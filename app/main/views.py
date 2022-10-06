# TODO: post page comment form development
# TODO: user page development 
# BUG: post page redirect url

# main route mappings

from flask import render_template, redirect, url_for, flash
from . import main_blueprint
from datetime import date
from .forms import SubscribeForm, SearchForm, ContactForm, CommentForm
from ..models import SubscribeModel
from .. import db

# - - - - - - - - - - - - - - - - - - - - home
@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    subscribe_form = SubscribeForm()                                # subscribe form object
    search_form = SearchForm()                                      # search form object

    # subscribe form submission handling
    if subscribe_form.validate_on_submit():                         # subscribe form successfully submitted
        subscriber = SubscribeModel.query.filter_by(email = subscribe_form.email.data).first()
        if subscriber is None:
            subscriber = SubscribeModel(name = str(subscribe_form.name.data).lower(), email = subscribe_form.email.data, date_subscribed = date.today())
            db.session.add(subscriber)
            db.session.commit()
            flash("{} subscribed successfully.".format(subscribe_form.email.data))
            return redirect(url_for('main.index'))                  # redirect to index
        else:
            flash("{} email already subscribed!".format(subscribe_form.email.data))

    # search form submission handling
    if search_form.validate_on_submit():                            # search form successfully submitted
        flash("searching result for \"{}\"".format(search_form.search.data))
        return redirect(url_for('main.index'))
    return render_template('index.html', subscribe = subscribe_form, search = search_form)


# - - - - - - - - - - - - - - - - - - - - user
@main_blueprint.route('/user/<username>')
def user(username):
    return render_template('user.html', username = username)


# - - - - - - - - - - - - - - - - - - - - post
@main_blueprint.route('/post/<title>', methods = ['GET', 'POST'])
def post(title):
    comment_form = CommentForm()
    if comment_form.validate_on_submit():                           # comment posted successfully
        print("Comment is: {}".format(comment_form.data))
        flash('comment posted successfull')
        redirect(url_for('main.post'))                              # BUG
    return render_template('post.html', comment = comment_form, title = title)


# - - - - - - - - - - - - - - - - - - - - about us
@main_blueprint.route('/about', methods=['GET', 'POST'])
def about():
    contact_form = ContactForm()                                    # about page form
    if contact_form.validate_on_submit():                           # contact form successfullty submitted
        flash('Message successfully submitted. You will get in touch soon.')
        return redirect(url_for('main.about'))                      # redirect to the same page
    return render_template('about.html', contact = contact_form)

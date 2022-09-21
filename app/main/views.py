# general route mappings

from crypt import methods
from flask import render_template, redirect, url_for, flash
from . import main_blueprint
from datetime import datetime
from .forms import Subscribe

# - - - - - - - - - - - - - - - - - - - - home
@main_blueprint.route('/', methods=['GET', 'POST'])
def index():
    subscribe_form = Subscribe()                            # create form object
    if subscribe_form.validate_on_submit():                 # form successfully submitted
        print(subscribe_form.email.data)
        flash('Thankyou for subscribing. You will get notified')
        return redirect(url_for('general.index'))           # redirect to index
    return render_template('index.html')

# - - - - - - - - - - - - - - - - - - - - user
@main_blueprint.route('/user/<username>')
def user(username):
    subscribe_form = Subscribe()                            # create form object
    if subscribe_form.validate_on_submit():                 # form successfully submitted
        print(subscribe_form.email.data)
        flash('Thankyou for subscribing. You will get notified')
        return redirect(url_for('general.index'))           # redirect to index
    return render_template('user.html', username = username)

# - - - - - - - - - - - - - - - - - - - - post
@main_blueprint.route('/post/<title>')
def post(title):
    return render_template('post.html', title = title)

# - - - - - - - - - - - - - - - - - - - - about us
@main_blueprint.route('/about')
def about():
    return render_template('about.html')
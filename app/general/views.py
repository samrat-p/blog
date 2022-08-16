# general route mappings

from crypt import methods
from flask import render_template, redirect, url_for, flash
from . import general_blueprint
from datetime import datetime
from .forms import Subscribe

 

# - - - - - - - - - - - - - - - - - - - - home
@general_blueprint.route('/', methods=['GET', 'POST'])
def index():
    subscribe_form = Subscribe()                            # create form object
    if subscribe_form.validate_on_submit():                 # form successfully submitted
        print(subscribe_form.email.data)
        flash('Thankyou for subscribing. You will get notified')
        return redirect(url_for('general.index'))           # redirect to index
    return render_template('index.html', form = subscribe_form, comment_datetime = datetime.utcnow(), flash_message = 'login successful', flash_type = None)

# - - - - - - - - - - - - - - - - - - - - user
@general_blueprint.route('/user/<username>')
def user(username):
    subscribe_form = Subscribe()                            # create form object
    if subscribe_form.validate_on_submit():                 # form successfully submitted
        print(subscribe_form.email.data)
        flash('Thankyou for subscribing. You will get notified')
        return redirect(url_for('general.index'))           # redirect to index
    return render_template('user.html', form = subscribe_form, comment_datetime = datetime.utcnow(), flash_message = 'login successful', flash_type = None)

# - - - - - - - - - - - - - - - - - - - - post
@general_blueprint.route('/post/<title>')
def post():
    return render_template('post.html', flash_message = 'login successful')

# - - - - - - - - - - - - - - - - - - - - about us
@general_blueprint.route('/about')
def about():
    return render_template('about.html')

# - - - - - - - - - - - - - - - - - - - - 
# TODO: moderator page need spacial permission to access.
# TODO: Use 2 step authentication to access moderator page
# 

# authentication route mappings
from crypt import methods
from flask import render_template, redirect, url_for, flash
from . import auth_blueprint
# from datetime import datetime
from ..models import SubscribeModel
from .forms import CreatePost

# - - - - - - - - - - - - - - - - - - - - moderator
@auth_blueprint.route('/moderator')
def moderator():
    subscribers = SubscribeModel.query.all()
    return render_template('moderator.html', subscribers = subscribers)

# - - - - - - - - - - - - - - - - - - - - create account
# @auth_blueprint.route('/signup')
# def signup():
#     return render_template('signup.html')

# - - - - - - - - - - - - - - - - - - - - login
@auth_blueprint.route('/login')
def login():
    return render_template('login.html')


# - - - - - - - - - - - - - - - - - - - - create post
# TODO: authentication requires
@auth_blueprint.route('/createpost', methods = ['GET', 'POST'])
def createpost():
    createpost_form = CreatePost()

    # create post form successfully submitted
    if createpost_form.validate_on_submit():
        # TODO: render data in database model
        flash(f'post created successfully by')
        return redirect(url_for('main.index'))
    
    # modify post form successfully submitted
    # TODO: modifypost form intregretion

    return render_template('createpost.html', form = createpost_form)

# authentication route mappings
from flask import render_template, redirect, url_for, flash
from . import auth_blueprint
from datetime import datetime

# - - - - - - - - - - - - - - - - - - - - moderator
@auth_blueprint.route('/moderator')
def moderator():
    return render_template('moderator,html')

# - - - - - - - - - - - - - - - - - - - - create account
@auth_blueprint.route('/signup')
def signup():
    return render_template('signup.html')

# - - - - - - - - - - - - - - - - - - - - login
@auth_blueprint.route('/login')
def login():
    return render_template('login.html')

# - - - - - - - - - - - - - - - - - - - - create post
@auth_blueprint.route('/createpost')
def createpost():
    return render_template('createpost.html')

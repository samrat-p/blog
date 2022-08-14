# general route mappings

from flask import render_template
from . import general_blueprint

# - - - - - - - - - - - - - - - - - - - - home
@general_blueprint.route('/')
@general_blueprint.route('/home')
def index():
    return render_template('index.html', flash_message = 'login successful', flash_type = None)

# - - - - - - - - - - - - - - - - - - - - post
@general_blueprint.route('/post/<title>')
def post():
    return render_template('post.html', flash_message = 'login successful')

# - - - - - - - - - - - - - - - - - - - - about us
@general_blueprint.route('/about')
def about():
    return render_template('about.html')

# - - - - - - - - - - - - - - - - - - - - 
# custom error handlers

from flask import render_template
from . import general_blueprint

# TODO: dynamic error pages handle
@general_blueprint.app_errorhandler(404)
def error(e):
    error_code, error_message = str(e).split(":")
    return render_template('error.html',
    error_code = error_code[0:4],
    error_message = error_message.split(".")[0])

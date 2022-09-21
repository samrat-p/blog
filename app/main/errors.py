# custom error handlers

from flask import render_template
from . import main_blueprint

# TODO: dynamic error pages handle
@main_blueprint.app_errorhandler(403)        # URL NOT FOUND
@main_blueprint.app_errorhandler(404)        # URL NOT FOUND
@main_blueprint.app_errorhandler(405)        # METHOD IS NOT ALLOWDED
def error(e):
    error_code, error_message = str(e).split(":")
    return render_template('error.html',
    error_code = error_code[0:4],
    error_message = error_message.split(".")[0])

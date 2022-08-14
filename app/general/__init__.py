from flask import Blueprint

general_blueprint = Blueprint('general', __name__)

from . import views, errors
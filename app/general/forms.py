# generel forms setup

import string
from unicodedata import name
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# subscribe form
class Subscribe(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Subscribe')



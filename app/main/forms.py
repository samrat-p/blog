# generel forms setup

from typing import Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length

# subscribe form
class SubscribeForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired(), length(max=120)])
    email = StringField('Email Address', validators=[DataRequired(), length(max=120)])
    submit = SubmitField('Subscribe')

# search form
class SearchForm(FlaskForm):
    search = StringField('Search Posts', validators=[DataRequired()])
    submit = SubmitField('Search')

# about page say hi
class ContactForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired(), length(max=200)])
    submit = SubmitField('Submit')

# post comment form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, length

# create post form
class CreatePost(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), length(max=50)])
    subtitle = StringField('Subtitile', validators=[DataRequired(), length(max=150)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Create')


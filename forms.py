from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    content = TextAreaField('Content')
    submit = SubmitField('Submit')

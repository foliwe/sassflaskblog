from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

class AddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Create Blog')

class EditForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Update Blog')
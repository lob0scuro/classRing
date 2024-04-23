from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class UserForm(FlaskForm):
    name = StringField("Student Name", validators=[DataRequired()])
    is_admin = BooleanField("Admin")
    submit = SubmitField("Register")


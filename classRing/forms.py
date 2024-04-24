from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, InputRequired

class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    is_admin = BooleanField("Admin")
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Register")


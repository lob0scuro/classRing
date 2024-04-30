from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField("Login")

class StudentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Queue')
    students = SelectField('Students', choices=[])
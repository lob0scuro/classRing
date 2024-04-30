from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length
from .models import Student
from flask_login import current_user

class LoginForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField("Login")

def student_query():
    return Student.query

class StudentForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    students = QuerySelectField(query_factory=lambda: Student.query.filter_by(admin_id=current_user.id).all(), allow_blank=True, get_label='name')
    submit = SubmitField('Queue')
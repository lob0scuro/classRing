from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, IntegerField, DateField, BooleanField
from wtforms.validators import InputRequired, DataRequired, Length, Email, ValidationError
from classRing.models import Users

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    password2 = PasswordField('Re-enter Password', validators=[DataRequired(), Length(min=5, max=20)])
    submit = SubmitField('Submit')
    
    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken, try another.')
        
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken, try another.')
        
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')



class CreateRing(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    due_date = DateField('Due date')
    value = IntegerField('Ring Value', validators=[DataRequired()])
    status = BooleanField('Completed')

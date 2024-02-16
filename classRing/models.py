from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from sqlalchemy import Integer, Date, String, Boolean



db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(userId):
    return Users.query.get(int(userId))

class Users(db.Model, UserMixin):
    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(String(50), nullable=False, unique=True)
    email = db.Column(String(50), nullable=False, unique=True)
    password = db.Column(String(255), nullable=False)
    

class Ring(db.Model):
    id = db.Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(String(100), nullable=False)
    category = db.Column(String(50), nullable=False)
    due_date = db.Column(Date) 
    value = db.Column(Integer)

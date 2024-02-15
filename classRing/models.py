from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager




db = SQLAlchemy()
login_manager = LoginManager()


@login_manager.user_loader
def load_user(userId):
    return Users.query.get(userId)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    
    
from flask import redirect, render_template, url_for, flash, Blueprint, request, session
from flask_login import UserMixin, LoginManager, login_required, login_user, logout_user
from classRing.models import db, Users
from classRing.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt



authBP = Blueprint('auth', __name__, url_prefix="/auth")

bcrypt = Bcrypt()


@authBP.route("/register", methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if request.method == "POST":
        username = form.username.data
        email = form.email.data
        pw1 = form.password.data
        pw2 = form.password2.data
        if pw2 == pw1:
            user = Users(username=username, password=bcrypt.generate_password_hash(pw1), email=email)
            db.session.add(user)
            db.session.commit()
            flash("Account Registered!")
            return redirect(url_for('auth.login'))
        else:
            flash("Passwords don't match, try again.")
        
    return "<h1 style='text-align: center; color: navy; margin-top: 25px;'>Class Ring</h1>\n<h3 style='text-align: center; color: navy; margin-top: 25px;'>Register</h3>"


@authBP.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    return "<h1 style='text-align: center; color: navy; margin-top: 25px;'>Class Ring</h1>\n<h3 style='text-align: center; color: navy; margin-top: 25px;'>Login</h3>"
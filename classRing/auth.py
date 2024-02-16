from flask import redirect, render_template, url_for, flash, Blueprint, request, session
from flask_login import login_required, login_user, logout_user, current_user
from classRing.models import db, Users
from classRing.forms import RegistrationForm, LoginForm
from flask_bcrypt import Bcrypt



authBP = Blueprint('auth', __name__, url_prefix="/auth")

bcrypt = Bcrypt()


@authBP.route("/register", methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
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
        
    return render_template('auth/register.html', form=form)


@authBP.route("/login", methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = Users.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=form.remember_me.data)
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials! Try again.')
    return render_template('auth/login.html', form=form)


@authBP.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
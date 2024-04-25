from flask import Blueprint, render_template, redirect, url_for, session, request, abort
from classRing import login_manager
from classRing.models import Student, Admin, db
from classRing.forms import RegistrationForm
from flask_login import login_user, logout_user, current_user, login_required


authBP = Blueprint("auth", __name__)
login_manager.login_view = "auth.login"

@authBP.route("/register", methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        new_user = Admin(name=name.capitalize(), password=password)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            print(f"Error: {e}")
            db.session.rollback()
    
    return render_template('auth/registration.html', form=form) 
           
@authBP.route('/', methods=('GET', 'POST'))            
@authBP.route('/login', methods=('GET', 'POST'))
def login():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        user = Admin.query.filter_by(name=name.capitalize())
        
        if not user:
            return "<h1>User not found</h1>"
        
        if user.password == password:
            login_user(user)
            next = request.args.get('next')
            
            
            return (next or redirect(url_for('main.index')))
        
    return render_template('auth/login.html', form=form)
        
@authBP.route('/logout')
@login_required
def logout():
    logout_user()
    return "you logged out."
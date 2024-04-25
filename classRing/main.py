from flask import Blueprint, render_template, redirect, url_for, session, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from classRing import login_manager
from classRing.forms import LoginForm, StudentForm
from classRing.models import Student, Admin, Ring, db


mainBP = Blueprint("main", __name__, url_prefix="/")

login_manager.login_view = '.login'
login_manager.login_message = 'Please log in to access the Dashboard'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)

@mainBP.route("/", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data

        user = Admin.query.filter_by(name=name.capitalize()).first()
        if not user:
            flash('User Not Found, Try Again')
            return redirect(url_for('.login'))
        
        if password == user.password:
            login_user(user)
            return redirect(url_for('.dash'))
        else:
            flash(f"Password for user: {name.capitalize()}, is incorrect. Try again")
            return redirect(url_for('.login'))

    return render_template("index.html", form=form)


@mainBP.route('/dash', methods=('GET', 'POST'))
@login_required
def dash():
    form = StudentForm()
    students = Student.query.filter_by(admin_id=current_user.id).all()
    if form.validate_on_submit():
        name = form.name.data
        try:
            queueStudent = Student.create_with_ring(name=name.capitalize(), admin_id=current_user.id)
        
            db.session.add(queueStudent)
            db.session.commit()
            flash(f"{queueStudent.name} added to Queue!")
        except Exception as e:
            flash(f"Error: {e}")
            db.session.rollback()


        
    return render_template('dash.html', form=form, students=students)




@mainBP.route("dash/delete/<int:sid>", methods=['DELETE'])
@login_required
def delete(sid):
    if request.method == 'DELETE':
        student = Student.query.get(int(sid))
        ring = Ring.query.get(int(sid))
        if not student:
            print("Student not found in database")
            return redirect(url_for('.dash'))
        try:
            db.session.delete(student)
            db.session.delete(ring)
            db.session.commit()
            print(f"{student.name} deleted from queue")
        except Exception as e:
            print(f"Error: {e}")
            db.session.rollback()
    return redirect(url_for('.dash'))




@mainBP.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
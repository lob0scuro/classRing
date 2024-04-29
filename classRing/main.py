from flask import Blueprint, render_template, redirect, url_for, session, request, flash, jsonify
from flask_login import login_required, login_user, logout_user, current_user
from classRing import login_manager
from classRing.forms import LoginForm, StudentForm
from classRing.models import Student, Admin, Ring, db



mainBP = Blueprint("main", __name__, url_prefix="/")

login_manager.login_view = '.login'
login_manager.login_message = 'Please log in to access the Dashboard'
login_manager.session_protection = "strong"

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
            flash('logged in!')
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
        return redirect(url_for('.dash'))


        
    return render_template('dash.html', form=form, students=students)

@mainBP.route("/platform", methods=('GET', 'POST'))
@login_required
def platform():
    students = Student.query.filter(Student.is_active==True, Student.admin_id==current_user.id).all()
    return render_template('platform.html', students=students)

@mainBP.route('/get_current_points/<int:sid>/', methods=('GET', 'POST'))
@login_required
def get_current_points(sid):
    student = Student.query.get(sid)
    points = student.ring.current_value
    
    return points



#CURRENT TASK
@mainBP.route('/points', methods=('GET', 'POST'))
@login_required
def countPoints():
    students = Student.query.filter(Student.is_active==True, Student.admin_id==current_user.id).all()
    points =[]
    for student in students:
        points.append(student.ring.current_value)
    total = sum(points)
    
    return render_template('points-overview.html', students=students, total=total)


@mainBP.route('/load-master', methods=('GET', 'POST', 'UPDATE'))
@login_required
def masterLoader():
    students = Student.query.filter(Student.is_active==True, Student.admin_id==current_user.id).all()
    points =[]
    for student in students:
        points.append(student.ring.current_value)
    total = sum(points)
    if request.method == 'GET':
        masterChamber = Admin.query.get(current_user.id)
        masterChamber.current_value = masterChamber.current_value + total
        for student in students:
            student.ring.current_value = 0
        db.session.commit()
        flash(f"{total} points loaded to {current_user.name}'s ring")
    return redirect(url_for('.dash'))
    
    


@mainBP.route('update/<int:sid>/<val>', methods=('GET', 'POST'))
@login_required
def update(sid, val):
    student = Student.query.get(sid)
    if str(val.lower()) == 'add':
        student.ring.current_value += 1
        db.session.commit()
    elif str(val.lower()) == 'sub':
        student.ring.current_value -= 1
        db.session.commit()
    else:
        flash("incorrent url param")
    return render_template('circles.html', student=student)

@mainBP.route("/activate/<int:sid>", methods=('POST', 'GET'))
@login_required
def activate(sid):
    form = StudentForm()
    students = Student.query.filter_by(admin_id=current_user.id).all()
    if request.method == "GET":
        student_to_activate = Student.query.get(sid)
        try:
            student_to_activate.is_active = True
            db.session.commit()
            flash(f'activated {student_to_activate.name}')
        except Exception as e:
            flash(f"Error: {e}")
            db.session.rollback()
        return redirect(url_for('.dash'))
    return render_template('dash.html', form=form, students=students)

@mainBP.route("/deactivate/<int:sid>", methods=('POST', 'GET'))
@login_required
def deactivate(sid):
    form = StudentForm()
    students = Student.query.filter_by(admin_id=current_user.id).all()
    if request.method == "GET":
        student_to_activate = Student.query.get(sid)
        try:
            student_to_activate.is_active = False
            db.session.commit()
            flash(f'deactivated {student_to_activate.name}')
        except Exception as e:
            flash(f"Error: {e}")
            db.session.rollback()
        return redirect(url_for('.dash'))
    return render_template('dash.html', form=form, students=students)





@mainBP.route("/delete/<int:sid>", methods=('POST', 'GET'))
@login_required
def delete(sid):
    form = StudentForm()
    students = Student.query.filter_by(admin_id=current_user.id).all()
    if request.method == 'GET':
        student = Student.query.get(sid)
        ring = Ring.query.get(sid)
        
        try:
            db.session.delete(student)
            db.session.delete(ring)
            db.session.commit()
            flash(f"{student.name} deleted from Queue!")
        except Exception as e:
            flash(f"Error: {e}")
            db.session.rollback()
        return redirect(url_for('.dash'))
    return render_template('dash.html', form=form, students=students)




@mainBP.route('/logout')
@login_required
def logout():
    logout_user()
    session.clear()
    flash(f"You have been logged out")
    return redirect(url_for('.login'))
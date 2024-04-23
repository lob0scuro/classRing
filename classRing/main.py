from flask import Blueprint, render_template, redirect, url_for, session, request
from classRing.forms import UserForm
from classRing.models import Student, Admin, Ring, db

mainBP = Blueprint("main", __name__, url_prefix="/")

@mainBP.route("/", methods=('GET', 'POST'))
def dash():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data

        if form.is_admin.data:
            try:
                admin = Admin(name=name.capitalize())
                db.session.add(admin)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
                db.session.rollback()
        else:
            try:
                student = Student(name=name.capitalize())
                db.session.add(student)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
                db.session.rollback()
        
        
        
        return redirect(url_for('main.dash'))

    return render_template("index.html", form=form)
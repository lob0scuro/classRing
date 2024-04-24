from flask import Blueprint, render_template, redirect, url_for, session, request
from classRing.forms import UserForm
from classRing.models import Student, Admin, db

mainBP = Blueprint("main", __name__, url_prefix="/")

@mainBP.route("/", methods=('GET', 'POST'))
def dash():
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        is_admin = form.is_admin.data
        admin_id = Admin.query.filter_by(id=1).first()
        if is_admin:
            try:
                admin = Admin(name=name.capitalize())
                db.session.add(admin)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
                db.session.rollback()
        else:
            try:
                student = Student.create_with_ring(name=name.capitalize(), admin_id=admin_id.id)
                db.session.add(student)
                db.session.commit()
            except Exception as e:
                print(f"Error: {e}")
                db.session.rollback()
        
        
        
        return redirect(url_for('main.dash'))

    return render_template("index.html", form=form)
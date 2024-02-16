from flask import redirect, render_template, url_for, flash, Blueprint
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from classRing.models import db,  Users, Ring
from classRing.forms import CreateRing

mainBP = Blueprint('main', __name__, url_prefix="/main")


@mainBP.route("/")
@mainBP.route("/home")
@login_required
def home():
    
    return render_template('main/home.html')


@mainBP.route("/create_ring", methods=('GET', 'POST'))
def create_ring():
    form = CreateRing()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        due_date = form.due_date.data
        value = form.value.data
        ring = Ring(title=title, category=category, due_date=due_date, value=value)
        db.session.add(ring)
        db.session.commit()
        flash("Ring created successfully!")
        return redirect(url_for('main.home'))
    return render_template('main/create_ring.html', form=form)


@mainBP.route("/view_rings", methods=('GET', 'POST'))
def view_rings():
    pass
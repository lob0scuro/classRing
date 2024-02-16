from flask import redirect, render_template, url_for, flash, Blueprint
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from classRing.models import Users

mainBP = Blueprint('main', __name__, url_prefix="/main")


@mainBP.route("/")
@mainBP.route("/home")
@login_required
def home():
    
    return render_template('main/home.html')
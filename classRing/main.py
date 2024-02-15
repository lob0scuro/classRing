from flask import redirect, render_template, url_for, flash, Blueprint
from flask_login import login_required, login_user, logout_user

mainBP = Blueprint('main', __name__, url_prefix="/main")

@mainBP.route("/")
def home():
    
    return "<h1 style='text-align: center; color: navy; margin-top: 25px;'>Class Ring</h1>\n<h3 style='text-align: center; color: navy; margin-top: 25px;'>Home</h3>"
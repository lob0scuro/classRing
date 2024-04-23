import os
from flask import Flask
from instance.config import Config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config["SQLALCHEMY_DATABASE_URI"]
    app.config["SECRET_KEY"] = Config["SECRET_KEY"]

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from .models import db
    with app.app_context():
        db.init_app(app)


    from .main import mainBP
    app.register_blueprint(mainBP)


    return app
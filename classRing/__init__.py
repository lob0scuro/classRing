import os
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS
from instance.config import Config


login_manager = LoginManager()
cors = CORS()



def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config["SQLALCHEMY_DATABASE_URI"]
    app.config["SECRET_KEY"] = Config["SECRET_KEY"]

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from .models import db
    migrate = Migrate(app, db)
    with app.app_context():
        db.init_app(app)
        login_manager.init_app(app)
        migrate.init_app(app)
        cors.init_app(app)


    from .main import mainBP
    app.register_blueprint(mainBP)


    return app
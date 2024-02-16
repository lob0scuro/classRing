from flask import Flask
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SERECT_KEY='dev',
        DATABASE="sqlite:///test.db"
    )
    
    
    
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    
    from classRing.models import db, login_manager
    db.init_app(app)
    login_manager.init_app(app)
    
    from classRing.auth import bcrypt
    bcrypt.init_app(app)
   
    
    from . import auth
    app.register_blueprint(auth.authBP)
    
    from . import main
    app.register_blueprint(main.mainBP, url_prefix="/")
    
    return app
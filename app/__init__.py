from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from .database import db
# Ensure models are imported
from .models import User  # Make sure your models are imported


bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    
    if config_filename:
        app.config.from_pyfile(config_filename)
    else:
        # Database configuration
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To silence deprecation warning
        # Secret keys
        app.config['SECRET_KEY'] = 'your_secret_key'
        app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Create tables, make sure to import all models above
    from . import models
    with app.app_context():
        db.create_all()

    # Register blueprints
    from .routes import main as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app

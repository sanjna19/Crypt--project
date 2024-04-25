from flask_sqlalchemy import SQLAlchemy
from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    public_key = db.Column(db.Text, nullable=False)  
    private_key = db.Column(db.Text, nullable=False) 

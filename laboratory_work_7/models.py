from flask_login import UserMixin
from dbase import db

class User(UserMixin, db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(1000))
    name = db.Column(db.String(100))
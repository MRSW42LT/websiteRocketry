from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    username = db.Column(db.String(50))
    notes = db.relationship('Note')
    opinioes = db.relationship('Formulario')

class Formulario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    opiniao_data = db.Column(db.String(2000),db.ForeignKey('user.id'))
    email = db.Column(db.String(50), unique=False)
    nome = db.Column(db.String(50))
    
class ComentarioHome(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    data_home = db.Column(db.String(500))
    
class ComentarioPropellants(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    data_propellants = db.Column(db.String(500))
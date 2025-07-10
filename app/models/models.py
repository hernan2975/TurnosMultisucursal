
from app import db

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    direccion = db.Column(db.String(200))

class Profesional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    especialidad = db.Column(db.String(100))
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"))

class Turno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(20))
    hora = db.Column(db.String(10))
    sucursal_id = db.Column(db.Integer, db.ForeignKey("sucursal.id"))
    profesional_id = db.Column(db.Integer, db.ForeignKey("profesional.id"))

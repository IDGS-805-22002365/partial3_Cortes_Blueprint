from sqlalchemy import Column, Integer, String, Date
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


db=SQLAlchemy()
class Alumno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido_paterno = db.Column(db.String(100), nullable=False)
    apellido_materno = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    grupo = db.Column(db.String(50), nullable=False)

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(255), nullable=False)
    opcion_a = db.Column(db.String(255), nullable=False)
    opcion_b = db.Column(db.String(255), nullable=False)
    opcion_c = db.Column(db.String(255), nullable=False)
    opcion_d = db.Column(db.String(255), nullable=False)
    respuesta_correcta = db.Column(db.String(1), nullable=False)

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'), nullable=False)
    respuesta = db.Column(db.String(1), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasenia = db.Column(db.String(256), nullable=False)
    
    def get_id(self):
        return str(self.id)
    
class Maestro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    materia = db.Column(db.String(100), nullable=False)
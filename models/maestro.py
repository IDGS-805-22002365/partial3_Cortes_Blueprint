from models.init import db

class Maestro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    materia = db.Column(db.String(100), nullable=False)

from models.init import db

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pregunta = db.Column(db.String(255), nullable=False)
    opcion_a = db.Column(db.String(255), nullable=False)
    opcion_b = db.Column(db.String(255), nullable=False)
    opcion_c = db.Column(db.String(255), nullable=False)
    opcion_d = db.Column(db.String(255), nullable=False)
    respuesta_correcta = db.Column(db.String(1), nullable=False)

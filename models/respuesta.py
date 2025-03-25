from models.init import db

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alumno_id = db.Column(db.Integer, db.ForeignKey('alumno.id'), nullable=False)
    pregunta_id = db.Column(db.Integer, db.ForeignKey('pregunta.id'), nullable=False)
    respuesta = db.Column(db.String(1), nullable=False)
    calificacion = db.Column(db.Integer, nullable=False)

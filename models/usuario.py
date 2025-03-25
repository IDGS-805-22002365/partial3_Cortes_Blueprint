from models.init import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contrasenia = db.Column(db.String(256), nullable=False)

    def get_id(self):
        return str(self.id)

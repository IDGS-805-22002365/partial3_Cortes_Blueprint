import logging
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from datetime import datetime
from models import Alumno, Pregunta, Respuesta, db, Usuario
from forms import AlumnoForm, PreguntaForm, ExamenForm, RegisterForm, LoginForm

# Importar los blueprints
from routes.alumnos import alumnos_bp
from routes.auth import auth_bp
from routes.examen import examen_bp
from routes.main import main_bp
from routes.preguntas import preguntas_bp
from routes.maestros import maestros_bp


# Configurar el sistema de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Crear la aplicación Flask
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect(app)

# Inicializar la base de datos
db.init_app(app)

# Inicializar el LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"  # Asegúrate de que sea el blueprint correcto

# Configurar la carga del usuario
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# Registrar los blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(alumnos_bp) 
app.register_blueprint(examen_bp)
app.register_blueprint(main_bp)
app.register_blueprint(preguntas_bp)
app.register_blueprint(maestros_bp)


# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()
    logger.info("Aplicación iniciada y base de datos creada")

# Iniciar la aplicación
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        logger.error(f"Error al iniciar la aplicación: {e}")

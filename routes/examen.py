from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from datetime import datetime
from models.alumno import Alumno
from models.pregunta import Pregunta
from models.respuesta import Respuesta
from models.init import db
from forms import ExamenForm
import logging


examen_bp = Blueprint("examen", __name__, url_prefix="/examen")

logger = logging.getLogger("app")

@examen_bp.route('/realizar_examen', methods=['GET', 'POST'])
@login_required
def realizar_examen():
    form = ExamenForm()
    
    if form.validate_on_submit():
        nombre = form.nombre.data
        apellido_paterno = form.apellido_paterno.data
        
        alumno = Alumno.query.filter_by(nombre=nombre, apellido_paterno=apellido_paterno).first()
        
        if alumno:
            return redirect(url_for('examen.realizar_examen_preguntas', alumno_id=alumno.id))
        else:
            logger.warning(f"Intento de examen con alumno no registrado: {nombre} {apellido_paterno}")
            flash('El alumno no existe', 'error')
            return redirect(url_for('examen.realizar_examen'))
    
    return render_template('examen/realizar_examen.html', form=form)

@examen_bp.route('/realizar_examen_preguntas/<int:alumno_id>', methods=['GET', 'POST'])
def realizar_examen_preguntas(alumno_id):
    alumno = Alumno.query.get_or_404(alumno_id)
    preguntas = Pregunta.query.all()
    
    edad = datetime.now().year - alumno.fecha_nacimiento.year
    
    if request.method == 'POST':
        calificacion = 0
        for pregunta in preguntas:
            respuesta_alumno = request.form.get(f'pregunta_{pregunta.id}')
            
            nueva_respuesta = Respuesta(
                alumno_id=alumno_id,
                pregunta_id=pregunta.id,
                respuesta=respuesta_alumno,
                calificacion=1 if respuesta_alumno == pregunta.respuesta_correcta else 0
            )
            db.session.add(nueva_respuesta)
            
            if respuesta_alumno == pregunta.respuesta_correcta:
                calificacion += 1

        db.session.commit()
        logger.info(f"Examen completado por {alumno.nombre} {alumno.apellido_paterno}. Calificación: {calificacion}/{len(preguntas)}")
        flash(f'Examen completado. Calificación: {calificacion}/{len(preguntas)}', 'success')
        return redirect(url_for('examen/ver_calificaciones'))

    return render_template('examen/realizar_examen_preguntas.html', preguntas=preguntas, alumno=alumno, edad=edad)

@examen_bp.route('/ver_calificaciones', methods=['GET', 'POST'])
@login_required
def ver_calificaciones():
    if request.method == 'POST':
        grupo = request.form.get('grupo')
        alumnos = Alumno.query.filter_by(grupo=grupo).all()
        calificaciones = []
        for alumno in alumnos:
            respuestas = Respuesta.query.filter_by(alumno_id=alumno.id).all()
            calificacion = sum(respuesta.calificacion for respuesta in respuestas)
            calificaciones.append((alumno, calificacion))
        logger.info(f"Visualización de calificaciones para el grupo {grupo}")
        return render_template('examen/ver_calificaciones.html', calificaciones=calificaciones, grupo=grupo)
    return render_template('examen/ver_calificaciones.html')

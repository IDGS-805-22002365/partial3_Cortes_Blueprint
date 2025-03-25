from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Alumno
from forms import AlumnoForm
import logging

alumnos_bp = Blueprint('alumnos', __name__, url_prefix="/alumnos")

logger = logging.getLogger("app")  # O configura como necesites


@alumnos_bp.route("/agregar_alumno", methods=['GET', 'POST'])
@login_required
def agregar_alumno():
    form = AlumnoForm()
    if form.validate_on_submit():
        alumno = Alumno(
            nombre=form.nombre.data,
            apellido_paterno=form.apellido_paterno.data,
            apellido_materno=form.apellido_materno.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            grupo=form.grupo.data
        )
        db.session.add(alumno)
        db.session.commit()
        flash('Alumno agregado correctamente', 'success')
        return redirect(url_for('alumnos.listar_alumnos'))
    return render_template('alumno/agregar_alumno.html', form=form)

@alumnos_bp.route('/eliminar_alumno/<int:alumno_id>', methods=['POST'])
@login_required
def eliminar_alumno(alumno_id):
    alumno = Alumno.query.get_or_404(alumno_id)
    db.session.delete(alumno)
    db.session.commit()
    logger.info(f"Alumno eliminado por {current_user.usuario}: {alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno}")
    flash('Alumno eliminado correctamente', 'success')
    return redirect(url_for('main.index'))

@alumnos_bp.route('/actualizar_alumno/<int:alumno_id>', methods=['GET', 'POST'])
@login_required
def actualizar_alumno(alumno_id):
    alumno = Alumno.query.get_or_404(alumno_id)
    form = AlumnoForm(obj=alumno)
    
    if form.validate_on_submit():
        form.populate_obj(alumno)
        db.session.commit()
        logger.info(f"Alumno actualizado por {current_user.usuario}: {alumno.nombre} {alumno.apellido_paterno} {alumno.apellido_materno}")
        flash('Alumno actualizado correctamente', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('alumno/actualizar_alumno.html', form=form, alumno=alumno)   

@alumnos_bp.route('/listar_alumnos')
@login_required
def listar_alumnos():
    alumnos = Alumno.query.all()
    return render_template('alumno/listar_alumnos.html', alumnos=alumnos)


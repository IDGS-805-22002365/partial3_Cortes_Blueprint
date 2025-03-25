from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required,current_user
from models.pregunta import Pregunta
from models.init import db
from forms import PreguntaForm
import logging

preguntas_bp = Blueprint("preguntas", __name__, url_prefix="/preguntas")

logger = logging.getLogger("app")

@preguntas_bp.route('/agregar_pregunta', methods=['GET', 'POST'])
@login_required
def agregar_pregunta():
    form = PreguntaForm()
    if form.validate_on_submit():
        pregunta = Pregunta(
            pregunta=form.pregunta.data,
            opcion_a=form.opcion_a.data,
            opcion_b=form.opcion_b.data,
            opcion_c=form.opcion_c.data,
            opcion_d=form.opcion_d.data,
            respuesta_correcta=form.respuesta_correcta.data
        )
        db.session.add(pregunta)
        db.session.commit()
        logger.info(f"Pregunta agregada: {pregunta.pregunta}")
        logger.info(f"Pregunta agregada por {current_user.usuario}: {pregunta.pregunta}")
        flash('Pregunta agregada correctamente', 'success')
        return redirect(url_for('main.index'))
    return render_template('pregunta/agregar_pregunta.html', form=form)

@preguntas_bp.route('/eliminar_pregunta/<int:pregunta_id>', methods=['POST'])
@login_required
def eliminar_pregunta(pregunta_id):
    pregunta = Pregunta.query.get_or_404(pregunta_id)
    db.session.delete(pregunta)
    db.session.commit()
    logger.info(f"Pregunta eliminada por {current_user.usuario}: {pregunta.pregunta}")
    flash('Pregunta eliminada correctamente', 'success')
    return redirect(url_for('main.index'))

@preguntas_bp.route('/actualizar_pregunta/<int:pregunta_id>', methods=['GET', 'POST'])
@login_required
def actualizar_pregunta(pregunta_id):
    pregunta = Pregunta.query.get_or_404(pregunta_id)
    form = PreguntaForm(obj=pregunta)
    
    if form.validate_on_submit():
        form.populate_obj(pregunta)
        db.session.commit()
        logger.info(f"Pregunta actualizada por {current_user.usuario}: {pregunta.pregunta}")
        flash('Pregunta actualizada correctamente', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('pregunta/actualizar_pregunta.html', form=form, pregunta=pregunta)

@preguntas_bp.route('/listar_preguntas')
@login_required
def listar_preguntas():
    preguntas = Pregunta.query.all()
    return render_template('pregunta/listar_preguntas.html', preguntas=preguntas)

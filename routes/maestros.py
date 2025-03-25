from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.maestro import Maestro
from models.init import db
from forms import MaestroForm

maestros_bp = Blueprint("maestros", __name__, url_prefix="/maestros")

@maestros_bp.route("/")
def lista_maestros():
    maestros = Maestro.query.all()
    return render_template("maestros/lista_maestros.html", maestros=maestros)

@maestros_bp.route("/agregar", methods=["GET", "POST"])
def agregar_maestro():
    form = MaestroForm()
    if form.validate_on_submit():
        nuevo_maestro = Maestro(
            nombre=form.nombre.data,
            apellido=form.apellido.data,
            materia=form.materia.data
        )
        db.session.add(nuevo_maestro)
        db.session.commit()
        flash("Maestro agregado exitosamente", "success")
        return redirect(url_for("maestros.lista_maestros"))
    return render_template("maestros/agregar_maestro.html", form=form)

@maestros_bp.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_maestro(id):
    maestro = Maestro.query.get_or_404(id)
    form = MaestroForm(obj=maestro)
    if form.validate_on_submit():
        maestro.nombre = form.nombre.data
        maestro.apellido = form.apellido.data
        maestro.materia = form.materia.data
        db.session.commit()
        flash("Maestro actualizado", "success")
        return redirect(url_for("maestros.lista_maestros"))
    return render_template("maestros/editar_maestro.html", form=form, maestro=maestro)

@maestros_bp.route("/eliminar/<int:id>", methods=["POST"])
def eliminar_maestro(id):
    maestro = Maestro.query.get_or_404(id)
    db.session.delete(maestro)
    db.session.commit()
    flash("Maestro eliminado", "success")
    return redirect(url_for("maestros.lista_maestros"))

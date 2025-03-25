from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from models.usuario import Usuario
from models.init import db
from forms import LoginForm, RegisterForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = Usuario.query.filter_by(usuario=username).first()
        if user and user.contrasenia == password:
            login_user(user)
            return redirect(url_for("main.index"))
        else:
            flash("Usuario o contraseña incorrectos", "error")

    return render_template("auth/login.html", form=form)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        existing_user = Usuario.query.filter_by(usuario=username).first()
        if existing_user:
            flash("El nombre de usuario ya está en uso", "error")
            return redirect(url_for("auth.register"))

        new_user = Usuario(usuario=username, contrasenia=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registro exitoso. Por favor, inicia sesión.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

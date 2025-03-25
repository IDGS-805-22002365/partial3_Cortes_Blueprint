from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, RadioField,PasswordField
from wtforms.validators import DataRequired

class AlumnoForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    grupo = SelectField('Grupo', choices=[('1', 'Grupo 1'), ('2', 'Grupo 2'),('3', 'Grupo 3'),('4', 'Grupo 4')], validators=[DataRequired()])
    submit = SubmitField('Guardar')

class PreguntaForm(FlaskForm):
    pregunta = StringField('Pregunta', validators=[DataRequired()])
    opcion_a = StringField('Opción A', validators=[DataRequired()])
    opcion_b = StringField('Opción B', validators=[DataRequired()])
    opcion_c = StringField('Opción C', validators=[DataRequired()])
    opcion_d = StringField('Opción D', validators=[DataRequired()])
    respuesta_correcta = SelectField('Respuesta Correcta', choices=[('a', 'A'), ('b', 'B'), ('c', 'C'), ('d', 'D')], validators=[DataRequired()])
    submit = SubmitField('Agregar Pregunta')

class ExamenForm(FlaskForm):
    nombre = StringField('Nombre', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    submit = SubmitField('Buscar Alumno')
class RegisterForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Registrarse")

class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired()])
    password = PasswordField("Contraseña", validators=[DataRequired()])
    submit = SubmitField("Iniciar Sesión")
    
class MaestroForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    materia = StringField("Materia", validators=[DataRequired()])
    submit = SubmitField("Guardar")

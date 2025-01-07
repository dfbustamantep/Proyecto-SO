from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired

class CreateProcessForm(FlaskForm):
    username = StringField("Nombre del usuario",validators=[DataRequired()])
    password = PasswordField("Contrasenia",validators=[DataRequired()])
    submit = SubmitField("Enviar datos",validators=[DataRequired()])
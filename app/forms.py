from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField,IntegerField,SelectMultipleField,SelectField
from wtforms.validators import DataRequired

class CreateProcesForm(FlaskForm):
    username = IntegerField("Tamaño del proceso",validators=[DataRequired()])
    recursos = SelectMultipleField("Recursos",validators=[DataRequired()])
    hilos = IntegerField("Hilos",validators=[DataRequired()])
    preminencia = SelectField("Preminencia",validators=[DataRequired()],choices=[('Si'), ('No')])
    submit = SubmitField("Crear proceso")
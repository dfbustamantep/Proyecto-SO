from flask_wtf import FlaskForm
from wtforms.fields import StringField,PasswordField,SubmitField,IntegerField,SelectMultipleField,SelectField
from wtforms.validators import DataRequired

class CreateProcesForm(FlaskForm):
    tamanio = IntegerField("Tamaño del proceso",validators=[DataRequired()])
    # coerce Convertir valores seleccionados a enteros
    recursos = SelectMultipleField("Recursos",validators=[DataRequired()])
    hilos = IntegerField("Hilos",validators=[DataRequired()])
                                                                        #Primer elemento de la tupla valor que se envia al servidor,segundo elemento texto que se muestra en el formulario
    preminencia = SelectField("Preminencia",validators=[DataRequired()],choices=[('No', 'No'), ('Si', 'Si')])
    submit = SubmitField("Crear proceso")
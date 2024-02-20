from wtforms import Form
from wtforms import StringField, TelField, IntegerField,RadioField

from wtforms import validators
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    ing = StringField('Ingles',[
        validators.DataRequired(message='El campo es obligatorio'),
        validators.length(min=2,max=25, message='Ingresa una palabra valida')
    ])
    esp = StringField("Español",[
        validators.DataRequired(message='El campo es oligatorio'),
        validators.length(min=2,max=25, message='Ingresa una palabra valida')
    ])
    
    buscar = StringField("Buscar",[
        validators.DataRequired(message='El campo es oligatorio'),
        validators.length(min=2,max=25, message='Ingresa una palabra')
    ])
    
    idioma = RadioField('Idioma', choices=[('Ingles', 'Ingles'), ('Español', 'Español')])
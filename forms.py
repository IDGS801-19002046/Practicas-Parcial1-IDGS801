from wtforms import Form

from wtforms import StringField,TelField,IntegerField

from wtforms.validators import DataRequired,Email



class UserForm(Form):
   
    p1x = IntegerField("p1x")
    p2x= IntegerField("p2x")
    p1y = IntegerField("p1y")
    p2y = IntegerField('p2y')
    resultado = IntegerField('resultado')
    
    
    
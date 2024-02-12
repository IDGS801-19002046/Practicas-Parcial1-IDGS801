
from wtforms import Form
from wtforms import SelectField, RadioField


class Resistencias(Form):
    b1 = SelectField('Color 1', 
                         choices=[(0, 'Negro'), (1, 'Cafe'), (2,'Rojo'),
                                  (3, 'Naranja'), (4, 'Amarillo'), (5, 'Verde'),
                                  (6, 'Azul'), (7, 'Morado'), (8, 'Gris'),
                                  (9, 'Blanco')])
    b2 = SelectField('Color 2', 
                         choices=[(0, 'Negro'), (1, 'Cafe'), (2,'Rojo'),
                                  (3, 'Naranja'), (4, 'Amarillo'), (5, 'Verde'),
                                  (6, 'Azul'), (7, 'Morado'), (8, 'Gris'),
                                  (9, 'Blanco')])
    b3 = SelectField('Color 3', 
                        choices=[(1, 'Negro'), (10, 'Cafe'), (100, 'Rojo'),
                                  (1000, 'Naranja'), (10000, 'Amarillo'), (100000, 'Verde'),
                                  (1000000, 'Azul'), (10000000, 'Morado'), (100000000, 'Gris'),
                                  (1000000000, 'Blanco')])
    tol = RadioField('Tolerancia', choices=[(.05, 'Dorado'), (.1, 'Plateado')])
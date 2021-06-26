from flask_wtf import Form
from wtforms import DecimalField, HiddenField, RadioField
from wtforms.validators import DataRequired

class VectorForm(Form):
    count = HiddenField('vector_counter')
    mag = DecimalField('distance', validators=[DataRequired()], places=2, default=0)
    ns = RadioField('north_south', choices = [(0, 'north'), ( 1, 'south')], default=0)
    degree = DecimalField('degree', validators=[DataRequired()], places=2, default=0)
    minute = DecimalField('minute', validators=[DataRequired()], places=2, default=0)
    ew = RadioField('east_west', choices = [(0,'west'), (1, 'east')], default=0)
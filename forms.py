from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NaamFormulier(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
    verzenden = SubmitField('Verzenden')
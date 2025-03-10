from flask_wtf import FlaskForm
from wtforms import FileField, IntegerField, StringField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import DataRequired

class NaamFormulier(FlaskForm):
    naam = StringField('Naam', validators=[DataRequired()])
    verzenden = SubmitField('Verzenden')
class BungalowForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    aantalPersonen = IntegerField('AantalPersonen', validators=[DataRequired()]) 
    prijs = DecimalField('Prijs', validators=[DataRequired()])
    fileLocation = FileField('FileLocation', validators=[DataRequired()])
    submit = SubmitField('Submit')

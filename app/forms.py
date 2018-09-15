from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class UnbabelForm(FlaskForm):
    input_field = StringField('Text to Translate', validators=[DataRequired()])
    submit = SubmitField('Translate to Spanish(ES)')

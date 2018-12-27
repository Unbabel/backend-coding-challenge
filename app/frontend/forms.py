from flask_wtf import FlaskForm
from wtforms import StringField, validators


class SubmitTranslationsForm(FlaskForm):
    # TODO : Add validator for special chars
    input_message = StringField(
        'Text Input',
        [validators.Length(min=0, max=256), validators.InputRequired()]
    )

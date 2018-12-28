from flask import Blueprint, render_template, request, flash, url_for, redirect

from app.core.utils import get_translations, store_translation_in_database
from app.frontend.forms import SubmitTranslationsForm
from app.tasks import send_translation_to_unbabel

mod = Blueprint("frontend", __name__)


@mod.route('/', methods=['GET', 'POST'])
def home_page():

    form = SubmitTranslationsForm()

    if request.method == 'POST' and form.validate_on_submit():
        try:
            translation = store_translation_in_database(form.input_message.data)
            send_translation_to_unbabel.delay(translation.uuid, translation.source_text)
            flash('Translation added with success', category='success')
        except Exception:
            flash('An error happen while adding the translation. Please try again later.', category='danger')
            
    descend = True if request.args.get('order') == 'desc' else False
    return render_template('index.html', form=form, translations=get_translations(descend=descend), descend=descend)


from flask import Blueprint, request

from app.core.models import Translation
from app.core.utils import update_translation

mod = Blueprint("backend", __name__)


@mod.route('/translation', methods=['POST'])
def translation_callback():
    update_translation(request.form.get('uid'),
                       status=Translation.TRANSLATED,
                       translated_text=request.form.get('translated_text'))
    return "", 200

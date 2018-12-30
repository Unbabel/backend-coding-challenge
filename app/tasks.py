import logging

from app.core.models import Translation
from app.core.unbabel import send_request_to_unbabel
from app.core.utils import update_translation
from . import celery, create_app

logger = logging.getLogger(__name__)


@celery.task
def send_translation_to_unbabel(uid, input_text):
    with create_app().app_context():
        response = send_request_to_unbabel(uid, input_text)
        if response is not None and response.status_code == 201:
            update_translation(uid, status=Translation.PENDING)
            logger.info("Message is Pending now - waiting for the translation")
        else:
            update_translation(uid, status=Translation.CANCELLED)
            logger.info("Message had a problem when sending to Unbabel servers")

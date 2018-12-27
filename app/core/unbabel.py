import requests
import json
import settings
import logging

logger = logging.getLogger(__name__)


def get_callback_url():
    if settings.CALLBACK_IP_ADDRESS is not None:
        return "http://{}/api/translation".format(settings.CALLBACK_IP_ADDRESS)
    else:
        return settings.CALLBACK_URL


def send_request_to_unbabel(uid, source_text):
    """
    Sends the translation to Unbabel Service to be processed

    :param uid: UID tp identify the message
    :param source_text: Text to be translated
    :return: Response from unbabel
    """

    headers = {
        "Authorization": "ApiKey {}:{}".format(settings.UNBABEL_USERNAME, settings.UNBABEL_PASSWORD),
        "Content-Type": "application/json"
    }

    data = {
        "text": source_text,
        "source_language": settings.SOURCE_TRANSLATION_LANGUAGE,
        "target_language": settings.TARGET_TRANSLATION_LANGUAGE,
        "callback_url": get_callback_url(),
        "uid": uid
    }
    return requests.post(settings.UNBABEL_TRANSLATION_URL, data=json.dumps(data), headers=headers)


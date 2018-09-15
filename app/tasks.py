import requests
from app import make_celery
from config import Config

celery = make_celery()


@celery.task
def send_text(source_text):
    payload = {
        'text': source_text,
        'source_language': 'en',
        'target_language': 'pt',
        'text_format': 'text',
    }
    response = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
    if response.status_code == 201:
        return response


@celery.task
def save_translation(response):
    pass

import requests
from app import make_celery
from config import Config

celery = make_celery()

payload = {
    'text': 'Hello world',
    'source_language': 'en',
    'target_language': 'pt',
    'text_format': 'text',
}

# r = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
# print(r)


@celery.task
def add(x, y):
    return x + y

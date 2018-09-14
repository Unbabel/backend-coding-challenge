import requests
from celery import Celery
from config import Config

app = Celery('tasks', broker=Config.REDISTOGO_URL)

payload = {
    'text': 'Hello world',
    'source_language': 'en',
    'target_language': 'pt',
    'text_format': 'text',
}

# r = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
# print(r)


@app.task
def add(x, y):
    return x + y

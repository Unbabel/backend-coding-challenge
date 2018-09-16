import requests
from flask import flash
from app import make_celery
from app.models import Translation
from database import db
from config import Config

celery = make_celery()


@celery.task
def send_request(source_text):
    payload = {
        'text': source_text,
        'source_language': 'en',
        'target_language': 'es',
        'text_format': 'text',
    }
    response = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
    if response.status_code == 201:
        data = response.json()
        save_request.delay(data)
    else:
        flash('Error')
        

@celery.task
def save_request(data):
    translation = Translation(
        source_text=data['text'],
        translated_text='requested',
        uid=data['uid'],
        status=data['status'],
    )
    db.session.add(translation)
    db.session.commit()


@celery.task
def get_periodic_request():
    translations = Translation.query.all()

    for translation in translations:
        tr_check_url = Config.URL + translation.uid
        response = requests.get(tr_check_url, headers=Config.HEADERS)
        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'completed':
                update_request.delay(data['uid'], 'translated', data['translatedText'])
            elif data['status'] == 'translating':
                update_request.delay(data['uid'], 'pending', data['translatedText'])


@celery.task
def update_request(uid, status, text):
    translation = Translation.query.filter_by(uid=uid).first()
    translation.status = status
    translation.translated_text = text
    db.session.commit()

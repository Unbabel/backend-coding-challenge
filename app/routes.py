from app import app
from flask import render_template
from app.forms import UnbabelForm
from config import Config
import requests


payload = {
    'text': 'Hello world',
    'source_language': 'en',
    'target_language': 'pt',
    'text_format': 'text',
}
# r = requests.post(Config.URL, json=payload, headers=Config.HEADERS)
# print(r)


@app.route('/')
@app.route('/index')
def index():
    form = UnbabelForm()
    return render_template('index.html', title='Unbabel Coding Challenge', form=form)

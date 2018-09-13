from app import app
from flask import render_template
from app.forms import UnbabelForm
import requests


url = 'https://sandbox.unbabel.com/tapi/v2/translation/'
headers = {
    'Authorization': 'ApiKey fullstack-challenge:9db71b322d43a6ac0f681784ebdcc6409bb83359',
    'Content-Type': 'application/json',
}
payload = {
    'text': 'Hello world',
    'source_language': 'en',
    'target_language': 'pt',
    'text_format': 'text',
}
r = requests.post(url, json=payload, headers=headers)
print(r)


@app.route('/')
@app.route('/index')
def index():
    form = UnbabelForm()
    return render_template('index.html', title='Unbabel Coding Challenge', form=form)

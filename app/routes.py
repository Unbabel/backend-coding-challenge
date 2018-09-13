from app import app
from flask import render_template
from app.forms import UnbabelForm
from unbabel.api import UnbabelApi


uapi = UnbabelApi(username='fullstack-challenge', api_key='9db71b322d43a6ac0f681784ebdcc6409bb83359', sandbox=True,)

to_translate = 'Hello world!'
target_language = 'pt'
uapi.post_translations(text=to_translate, target_language=target_language,)


@app.route('/')
@app.route('/index')
def index():
    form = UnbabelForm()
    return render_template('index.html', title='Unbabel Coding Challenge', form=form)

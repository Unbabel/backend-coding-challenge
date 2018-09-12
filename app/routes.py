from app import app
from flask import render_template
from app.forms import UnbabelForm


@app.route('/')
@app.route('/index')
def index():
    form = UnbabelForm()
    return render_template('index.html', title='Unbabel Coding Challenge', form=form)

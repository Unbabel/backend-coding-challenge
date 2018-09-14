from flask import Blueprint, render_template
from app.forms import UnbabelForm

bp = Blueprint('app', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    form = UnbabelForm()
    return render_template('index.html', title='Unbabel Coding Challenge', form=form)
from flask import Blueprint, render_template
from flask.views import MethodView
from app.forms import UnbabelForm


bp = Blueprint('app', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    form = UnbabelForm()
    return render_template('index.html', title='Unbabel Coding Challenge', form=form)


class Index(MethodView):
    def post(self):
        form = UnbabelForm()
        if form.validate_on_submit():
            add.delay(4, 15)


from app.tasks import add

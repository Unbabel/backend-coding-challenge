import app
from app import db
from app.models import Translation

app = app.create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Translation': Translation, }

from app import app, db
from app.models import Translation


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Translation': Translation, }

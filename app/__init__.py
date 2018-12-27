from celery import Celery
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

from app.core.models import db

import settings

celery = Celery(__name__,
                broker=settings.CELERY_BROKER_URL,
                include=['app.tasks'])

migrate = Migrate()

if settings.CALLBACK_IP_ADDRESS is None and settings.CALLBACK_URL is None:
    raise Exception("Please review README and export CALLBACK_IP_ADDRESS or CALLBACK_URL")


def create_app():

    app = Flask(__name__)
    app.config['DEBUG'] = settings.DEBUG
    app.config['HOST'] = "127.0.0.1"

    # Celery
    app.config['CELERY_BROKER_URL'] = settings.CELERY_BROKER_URL
    app.config['CELERY_RESULT_BACKEND'] = settings.CELERY_RESULT_BACKEND
    celery.conf.update(app.config)

    # Frontend CSRF
    app.config['WTF_CSRF_ENABLED'] = settings.WTF_CSRF_ENABLED
    app.config['SECRET_KEY'] = settings.SECRET_KEY

    # Bootstrap
    Bootstrap(app)

    # Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@{}:{}/{}'.format(
        settings.DATABASE_USERNAME,
        settings.DATABASE_PASSWORD,
        settings.DATABASE_HOST,
        settings.DATABASE_PORT,
        settings.DATABASE_NAME
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    from app.frontend.routes import mod as frontend_mod
    app.register_blueprint(frontend_mod)

    from app.backend.routes import mod as backend_mod
    app.register_blueprint(backend_mod, url_prefix='/api')

    return app

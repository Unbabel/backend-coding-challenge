from flask import Flask
from flask_restful import Api
from celery import Celery
from config import Config
from database import database_init

CELERY_TASK_LIST = [
    'app.tasks'
]


def make_celery(app=None):
    app = app or create_app()
    celery = Celery(app.import_name,
                    broker=Config.REDISTOGO_URL,
                    include=CELERY_TASK_LIST,
                    )
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
    return celery


def create_app(config_class=Config):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(config_class)
    database_init(app)

    from app.views import Index
    api.add_resource(Index, '/')

    return app


from app import models

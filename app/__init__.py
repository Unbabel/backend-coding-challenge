from flask import Flask
from config import Config
from database import database


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    database(app)

    from app.views import bp as index_bp
    app.register_blueprint(index_bp)

    return app


from app import models

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def database_init(app):
    db.init_app(app)
    migrate.init_app(app, db)

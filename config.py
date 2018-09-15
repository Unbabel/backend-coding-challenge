

class Config(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = '86xd8Zx94xd7x12o}x18f28f517xbf14c9ba1bx81b888ui1ortbb4'

    POSTGRES = {
        'user': 'postgres',
        'pw': 'postgres',
        'db': 'unbabel_database',
        'host': 'localhost',
        'port': '5432',
    }
    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis
    LISTEN = ['default']
    REDISTOGO_URL = 'redis://localhost:6379'

    # To start celery worker and beater:
    # celery -A app.tasks worker -B --loglevel=info
    CELERYBEAT_SCHEDULE = {
        'runs-every-15-seconds': {
            'task': 'app.tasks.get_periodic_request',
            'schedule': 15.0,
        }
    }

    # Unbabel API
    URL = 'https://sandbox.unbabel.com/tapi/v2/translation/'
    HEADERS = {
        'Authorization': 'ApiKey fullstack-challenge:9db71b322d43a6ac0f681784ebdcc6409bb83359',
        'Content-Type': 'application/json',
    }

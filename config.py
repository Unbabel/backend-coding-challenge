

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '\x86\xd8Z\x94\xd7\x12o}\x18\xf28\xf5\x17~\xbf\x14\xc9\x8b\xa1b\x81\xb8\x88\xb4'

    POSTGRES = {
        'user': 'postgres',
        'pw': 'password',
        'db': 'unbabel_database',
        'host': 'localhost',
        'port': '5432',
    }

    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False

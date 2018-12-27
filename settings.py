import os

DEBUG = os.environ.get("DEBUG", True)

UNBABEL_TRANSLATION_URL = os.environ.get("UNBABEL_TRANSLATION_URL", "https://sandbox.unbabel.com/tapi/v2/translation/")
UNBABEL_USERNAME = os.environ.get("UNBABEL_USERNAME", "fullstack-challenge")
UNBABEL_PASSWORD = os.environ.get("UNBABEL_PASSWORD", "9db71b322d43a6ac0f681784ebdcc6409bb83359")

CALLBACK_IP_ADDRESS = os.environ.get("CALLBACK_IP_ADDRESS", None)
CALLBACK_URL = os.environ.get("CALLBACK_URL", None)

DATABASE_HOST = os.environ.get("DATABASE_HOST", "127.0.0.1")
DATABASE_PORT = os.environ.get("DATABASE_PORT", "5432")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME", "test")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "test")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "test_db")

CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL", "redis://0.0.0.0:6379")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://0.0.0.0:6379")

SECRET_KEY = os.environ.get("SECRET_KEY", "wHNwYaqU83SR8dIfTIEH")
WTF_CSRF_ENABLED = os.environ.get("WTF_CSRF_ENABLED", True)

SOURCE_TRANSLATION_LANGUAGE = os.environ.get("SOURCE_TRANSLATION_LANGUAGE", "en")
TARGET_TRANSLATION_LANGUAGE = os.environ.get("TARGET_TRANSLATION_LANGUAGE", "es")
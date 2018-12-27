
import uuid
import settings

from app.core.models import Translation, db


def translation_uuid_exists(identifier):
    """
    Validate if the uuid is not in the Database
    :param identifier: String (uuid) with unique identifier
    :return: True if there aren't uuid in the database
    """
    return db.session.query(Translation).filter(Translation.uuid == identifier).first() is not None


def generate_uuid():
    """
    Get a valid uid to store in the Database
    :return:
    """
    identifier = str(uuid.uuid4())
    return identifier if not translation_uuid_exists(identifier) else generate_uuid()


def store_translation_in_database(source_text):
    """
    Store Translation in the Database
    :return: translation object
    """
    translation = Translation(uuid=generate_uuid(),
                              source_text=source_text,
                              source_language=settings.SOURCE_TRANSLATION_LANGUAGE,
                              target_language=settings.TARGET_TRANSLATION_LANGUAGE)
    db.session.add(translation)
    db.session.commit()
    return translation


def update_translation(uid, status=None, translated_text=None):
    if translation_uuid_exists(uid):
        query = db.session.query(Translation).filter(Translation.uuid == uid)

        if status is not None:
            query.update({'status': status})

        if translated_text is not None:
            query.update({'translated_text': translated_text})

        db.session.commit()
        db.session.flush()


def get_translations():
    return [x.json() for x in db.session.query(Translation).all()]

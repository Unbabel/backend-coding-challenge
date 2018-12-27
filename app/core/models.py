
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import ChoiceType

db = SQLAlchemy()


class Translation(db.Model):

    __tablename__ = 'translation'

    uuid = db.Column(db.String(36), primary_key=True)

    source_text = db.Column(db.String(256), nullable=False)
    translated_text = db.Column(db.String(1024), nullable=True)

    source_language = db.Column(db.String(2), nullable=False)
    target_language = db.Column(db.String(2), nullable=False)

    REQUESTED = 'REQUESTED'
    PENDING = 'PENDING'
    TRANSLATED = 'TRANSLATED'
    CANCELLED = 'CANCELLED'

    STATUS_TYPES = [
        (REQUESTED, u'Requested'),
        (PENDING, u'Pending'),
        (TRANSLATED, u'Translated'),
        (CANCELLED, u'Cancelled'),
    ]

    status = db.Column(ChoiceType(STATUS_TYPES), nullable=False, default=REQUESTED)

    def __repr__(self):
        return '<Translation "{}" - From {} To {}>'.format(self.source_text,
                                                           self.source_language,
                                                           self.target_language)

    def json(self):
        return {c.name: getattr(self, c.name) if getattr(self, c.name) is not None else '' for c in
                self.__table__.columns}

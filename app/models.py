from app import db


class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_text = db.Column(db.String(255), nullable=False)
    translated_text = db.Column(db.String(255), nullable=False)
    uid = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(15), nullable=False)

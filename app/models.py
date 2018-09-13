from app import db


class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    source_text = db.Column(db.String(255))
    translated_text = db.Column(db.String(255))
    uid = db.Column(db.String(20), unique=True)
    status = db.Column(db.String(15))

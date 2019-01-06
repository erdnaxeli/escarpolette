from escarpolette.extensions import db
from datetime import datetime


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    artist = db.Column(db.String(255))
    duration = db.Column(db.Integer)
    played = db.Column(db.Boolean, default=False)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return f"<Item {self.username}"

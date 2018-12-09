from escarpolette import db
from datetime import datetime


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    played = db.Column(db.Boolean)
    title = db.Column(db.String(255))
    url = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return f"<Item {self.username}"

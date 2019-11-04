from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.local import LocalProxy

from escarpolette.player import Player


db = SQLAlchemy()
player = Player()


def init_app(app):
    CORS(app)
    db.init_app(app)
    player.init_app(app)
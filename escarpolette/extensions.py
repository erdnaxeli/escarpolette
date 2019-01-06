from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.local import LocalProxy

from escarpolette.player import Player


db = SQLAlchemy()
player = Player()


def init_app(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///../db.sqlite"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)
    db.init_app(app)
    player.init_app(app)

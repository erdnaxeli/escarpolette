from fastapi import FastAPI
from flask_sqlalchemy import SQLAlchemy

from escarpolette.player import Player
from escarpolette.settings import Config


db = SQLAlchemy()
player = Player()


def init_app(app: FastAPI, config: Config):
    # CORS(app)
    # Migrate(app, db)
    player(config)

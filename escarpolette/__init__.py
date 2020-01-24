from typing import TextIO

from fastapi import FastAPI

from escarpolette import routers
from escarpolette.user import LoginManager
from escarpolette.settings import Config
from escarpolette import extensions, db


def create_app(config: Config):
    app = FastAPI(
        title="Escarpolette",
        version="0.1",
        description="Manage your party's playlist without friction",
    )

    routers.init_app(app)
    db.init_app(config)
    extensions.init_app(app, config)
    return app


# app.config.from_object(DefaultSettings(app))
# app.config.from_pyfile("application.cfg", silent=True)

# LoginManager().init_app(app)

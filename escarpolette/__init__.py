from fastapi import FastAPI

from escarpolette import routers
# from escarpolette.user import LoginManager
from escarpolette.settings import Config
from escarpolette import db
from escarpolette.player import get_player


def create_app(config: Config):
    app = FastAPI(
        title="Escarpolette",
        version="0.1",
        description="Manage your party's playlist without friction",
    )

    routers.init_app(app)
    db.init_app(config)
    get_player().init_app(config)

    @app.on_event("shutdown")
    def shutdown():
        get_player().shutdown()

    return app


# app.config.from_object(DefaultSettings(app))
# app.config.from_pyfile("application.cfg", silent=True)

# LoginManager().init_app(app)

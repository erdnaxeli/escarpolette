from fastapi import FastAPI

from escarpolette import routers
from escarpolette.user import LoginManager
from escarpolette.settings import Default as DefaultSettings
from escarpolette import extensions

app = FastAPI(
    title="Escarpolette",
    version="0.1",
    description="Manage your party's playlist without friction",
)

# app = Flask(__name__, instance_relative_config=True)
# app.config.from_object(DefaultSettings(app))
# app.config.from_pyfile("application.cfg", silent=True)

routers.init_app(app)
# extensions.init_app(app)
# LoginManager().init_app(app)

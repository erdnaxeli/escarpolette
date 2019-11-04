from flask import Flask

from escarpolette.api import api
from escarpolette.settings import Default as DefaultSettings
from escarpolette import extensions

app = Flask(__name__)
app.config.from_object(DefaultSettings(app))

extensions.init_app(app)
api.init_app(app)

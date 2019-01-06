from flask import Flask

from escarpolette.api import api
from escarpolette import extensions

app = Flask(__name__)

extensions.init_app(app)
api.init_app(app)

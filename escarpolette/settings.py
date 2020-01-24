from datetime import timedelta
from configparser import ConfigParser
from typing import TextIO


class Default:
    # Server
    HOST = "127.0.0.1"
    PORT = 8000

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DATABASE_URI = "sqlite:///"

    # Authentication
    REMEMBER_COOKIE_DURATION = timedelta(days=390)  # ~13 months


class Config(Default):
    def __init__(self, file: TextIO):
        config = ConfigParser().read_file(file)

        self.HOST = config.get("HOST", self.HOST)
        self.DATABASE_URI = config.get("DATABASE_URI", self.DATABASE_URI)

        self.SQLALCHEMY_DATABASE_URI = f"sqlite:///{app.instance_path}/db.sqlite"

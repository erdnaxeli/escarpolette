from flask import Flask


class Default:
    # Server
    HOST = "127.0.0.1"

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self, app: Flask):
        self.SQLALCHEMY_DATABASE_URI = f"sqlite:///{app.instance_path}/db.sqlite"

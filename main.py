#!/usr/bin/env python

from escarpolette import app

if __name__ == "__main__":
    app.run(host=app.config["HOST"])

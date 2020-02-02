# Changelog

## 0 (dev)

### 0.4.0

This realease breaks again the db migrations.
You need to delete you current database and recreate one.

Features:
* auto generate configuration on startup if not given (default path to `$XDG_CONFIG_HOME/escarpolette/escarpolette.conf`)
* create the database on startup and apply any missing migrations
* youtbe-dl version bump

Bugfix:
* an item with the same URL can be added again if the previous ones have been played

Internals:
* migration to [FastAPI](https://fastapi.tiangolo.com/). So long, Flask!
* no more usage of Alembic but plain SQL migrations files
* use [Uvicorn](https://www.uvicorn.org/) as web server

### 0.3.0

This release breaks the db migrations.
You need to delete your current database and recreate one.

* new model Playlist

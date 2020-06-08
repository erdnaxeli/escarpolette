from typing import Iterator

from fastapi import Depends
from sqlalchemy.orm import Session

from escarpolette import db
from escarpolette.models import Playlist


def get_db() -> Iterator[Session]:
    with db.get_db() as db_session:
        yield db_session


def get_current_playlist(db: Session = Depends(get_db)) -> Playlist:
    playlist = Playlist.get_current_playlist(db)
    return playlist

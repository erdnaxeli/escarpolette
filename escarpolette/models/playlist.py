from sqlalchemy.orm import relationship

from escarpolette.db import Base, get_db
from escarpolette.models.mixin import BaseModelMixin


class Playlist(BaseModelMixin, Base):
    __tablename__ = "playlists"

    items = relationship("Item", back_populates="playlist")

    @classmethod
    def get_current_playlist(cls, db_session):
        playlist = db_session.query(cls).order_by(Playlist.created_at.desc()).first()
        return playlist

    @classmethod
    def item_ended(cls):
        """Mark current playing item as played."""
        with get_db() as db_session:
            playlist = cls.get_current_playlist(db_session)

            played = True
            for item in playlist.items:
                if not item.played:
                    item.played = True
                    break

            db_session.commit()

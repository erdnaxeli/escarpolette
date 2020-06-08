from sqlalchemy.orm import Session, relationship
from sqlalchemy.ext.orderinglist import ordering_list

from escarpolette.db import Base, get_db
from escarpolette.models.mixin import BaseModelMixin


class Playlist(BaseModelMixin, Base):
    __tablename__ = "playlists"

    items = relationship(
        "Item",
        back_populates="playlist",
        order_by="Item.position",
        collection_class=ordering_list("position"),
    )

    @classmethod
    def get_current_playlist(cls, db_session: Session) -> "Playlist":
        playlist = db_session.query(cls).order_by(Playlist.created_at.desc()).first()
        return playlist

    @classmethod
    def item_ended(cls) -> None:
        """Mark current playing item as played."""
        with get_db() as db_session:
            playlist = cls.get_current_playlist(db_session)

            played = True
            for item in playlist.items:
                if not item.played:
                    item.played = True
                    break

            db_session.commit()

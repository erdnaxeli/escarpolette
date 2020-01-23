from fastapi import APIRouter, Depends
from flask_login import current_user
from werkzeug.exceptions import TooManyRequests

from escarpolette.db import get_db, Session
from escarpolette.models import Item
from escarpolette.player import get_player, Player
from escarpolette.schemas.item import ItemSchemaIn, ItemSchemaOut
from escarpolette.schemas.playlist import PlaylistSchemaOut
from escarpolette.tools import get_content_metadata
from escarpolette.rules import rules

router = APIRouter()


@router.get("/", response_model=PlaylistSchemaOut)
# @login_required
def get(db: Session = Depends(get_db)) -> PlaylistSchemaOut:
    playlist = PlaylistSchemaOut()

    for item in db.query(Item).order_by(Item.created_at).all():
        playlist.items.append(
            ItemSchemaOut(
                artist=item.artist,
                duration=item.duration,
                title=item.title,
                url=item.url,
            )
        )
        if item.played:
            playlist.idx += 1

    return playlist


@router.post("/", status_code=201, response_model=ItemSchemaOut)
# @login_required
def post(
    data: ItemSchemaIn,
    db: Session = Depends(get_db),
    player: Player = Depends(get_player),
) -> Item:
    metadata = get_content_metadata(data.url)
    item = Item(user_id=current_user.id, **metadata)

    if not rules.can_add_item(current_user, item):
        raise TooManyRequests

    db.add(item)
    db.flush()

    player.add_item(item.url)

    db.commit()

    return item

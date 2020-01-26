from typing import Dict, List

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, Field
from flask_login import current_user, login_required
from werkzeug.exceptions import BadRequest, TooManyRequests

from escarpolette.models import Item
from escarpolette.tools import get_content_metadata
from escarpolette.rules import rules

router = APIRouter()


class BaseItem(BaseModel):
    url: HttpUrl = Field(..., example="https://www.youtube.com/watch?v=bpA6fAz_r04")


class ItemIn(BaseItem):
    pass


class ItemOut(BaseItem):
    class Config:
        orm_mode = True

    artist: str = Field(..., example="Vic Dibitetto")
    duration: int = Field(..., example=94)
    title: str = Field(..., example="Anybody want cawfee?!")


class PlaylistOut(BaseModel):
    items: List[ItemOut] = []
    idx: int = 0


@router.get("/", response_model=PlaylistOut)
# @login_required
def get() -> PlaylistOut:
    playlist = PlaylistOut()

    for item in Item.query.order_by(Item.created_at).all():
        playlist.items.append(
            ItemOut(
                artist=item.artist,
                duration=item.duration,
                title=item.title,
                url=item.url,
            )
        )
        if item.played:
            playlist.idx += 1

    return playlist


@router.post("/", status_code=201, response_model=ItemOut)
# @login_required
def post(data: ItemIn) -> Item:
    metadata = get_content_metadata(data.url)
    item = Item(user_id=current_user.id, **metadata)

    if not rules.can_add_item(current_user, item):
        raise TooManyRequests

    db.session.add(item)
    db.session.flush()

    player.add_item(item.url)

    db.session.commit()

    return item

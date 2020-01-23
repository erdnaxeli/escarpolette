from typing import Dict, List

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl, Field
from flask import request
from flask_login import current_user, login_required
from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest, TooManyRequests

from escarpolette.extensions import db, player
from escarpolette.models import Item
from escarpolette.tools import get_content_metadata
from escarpolette.rules import rules

router = APIRouter()
ns = Namespace("items", description="Manage the playlist's items")

item = ns.model(
    "Item",
    {
        "artist": fields.String(readonly=True),
        "duration": fields.Integer(readonly=True),
        "title": fields.String(readonly=True),
        "url": fields.Url(
            absolute=True,
            example="https://www.youtube.com/watch?v=bpA6fAz_r04",
            required=True,
        ),
    },
)
playlist = ns.model(
    "Playlist", {"idx": fields.Integer, "items": fields.List(fields.Nested(item))}
)


class BaseItem(BaseModel):
    url: HttpUrl = Field(..., example="https://www.youtube.com/watch?v=bpA6fAz_r04")


class ItemIn(BaseItem):
    pass


class ItemOut(BaseItem):
    artist: str = Field(..., example="Vic Dibitetto")
    duration: int = Field(..., example=94)
    title: str = Field(..., example="Anybody want cawfee?!")


class PlaylistOut(BaseModel):
    items: List[ItemOut] = []
    idx: str = 0


# @ns.route("/")
# class Items(Resource):


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


@router.post("/")
# @ns.expect(item)
# @ns.marshal_with(item, code=201)
# @login_required
def post() -> Dict:
    data = request.json

    if data is None:
        raise BadRequest("Missing data")

    metadata = get_content_metadata(data["url"])
    item = Item(user_id=current_user.id, **metadata)

    if not rules.can_add_item(current_user, item):
        raise TooManyRequests

    db.session.add(item)
    db.session.flush()

    player.add_item(item.url)

    db.session.commit()

    return metadata

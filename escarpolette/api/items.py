from flask import jsonify, request
from flask_restplus import Namespace, Resource, fields
from werkzeug.exceptions import BadRequest

from escarpolette.extensions import db, player
from escarpolette.models import Item
from escarpolette.tools import get_url_metadata

ns = Namespace("items", description="Manage the playlist's items")

item = ns.model(
    "Item",
    {
        "artist": fields.String(required=False),
        "duration": fields.Integer(required=False),
        "title": fields.String(required=False),
        "url": fields.String(required=True),
    },
)

playlist = ns.model(
    "Playlist", {"idx": fields.Integer, "items": fields.List(fields.Nested(item))}
)


@ns.route("/")
class Items(Resource):
    @ns.marshal_list_with(playlist)
    def get(self):
        playlist = []
        playing_idx = 0

        for item in Item.query.order_by(Item.created_at).all():
            playlist.append(
                {
                    "artist": item.artist,
                    "duration": item.duration,
                    "title": item.title,
                    "url": item.url,
                }
            )
            if item.played:
                playing_idx += 1

        data = {"items": playlist, "idx": playing_idx}
        return data

    @ns.expect(item)
    @ns.marshal_with(item, code=201)
    def post(self):
        data = request.json

        if data is None:
            raise BaddRequest("Missing data")

        metadata = get_url_metadata(data["url"])
        item = Item(**metadata)
        db.session.add(item)
        db.session.flush()

        player.add_item(item.url)

        db.session.commit()

        return jsonify(metadata)

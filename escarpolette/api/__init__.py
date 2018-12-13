from flask import jsonify, request
from werkzeug.exceptions import BadRequest

from escarpolette import app, db, player
from escarpolette.models import Item
from escarpolette.tools import get_url_metadata


@app.route("/items", methods=["GET"])
def get_items():
    playlist = []
    playing_idx = -1

    for item in Item.query.order_by(Item.created_at).all():
        playlist.append({"title": item.title, "url": item.url})
        if not item.played:
            playing_idx += 1

    data = {"playlist": playlist, "playing_idx": playing_idx}
    return jsonify(data)


@app.route("/items", methods=["POST"])
def add_item():
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

from .items import router as item_router
from .player import router as player_router

from fastapi import FastAPI


def init_app(app: FastAPI) -> None:
    app.include_router(item_router, prefix="/item", tags=["items"])
    app.include_router(player_router, prefix="/player", tags=["player"])

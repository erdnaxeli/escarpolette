from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from escarpolette.extensions import player
from escarpolette.player import State

router = APIRouter()


class Player(BaseModel):
    state: State


@router.get("/", response_model=Player)
def get() -> Player:
    data = Player(state=player.get_state().name)
    return data


@router.patch("/", responses={400: {}})
def patch(data: Player) -> None:
    if data.state == State.PLAYING:
        player.play()
    elif data.state == State.PAUSED:
        player.pause()
    else:
        raise HTTPException(
            status_code=400, detail=f"The state {data.state} cannot be set"
        )

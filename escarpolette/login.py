from uuid import uuid4

import jwt
from fastapi import Cookie, Depends
from pydantic import BaseModel
from starlette.responses import Response

from escarpolette.settings import Config, get_current_config


MAX_AGE = 13 * 30 * 24 * 60 * 60  # 13 months
ALGORITHM = "HS256"


class User(BaseModel):
    id: str


def get_current_user(
    response: Response,
    token: str = Cookie(None),
    config: Config = Depends(get_current_config),
):
    if not token:
        current_user = User(id=str(uuid4()))
    else:
        claim = jwt.decode(token, config.SECRET_KEY, algorithms=[ALGORITHM])
        current_user = User(id=claim["user_id"])

    payload = {"user_id": current_user.id}
    sign = jwt.encode(payload, config.SECRET_KEY, algorithm=ALGORITHM)
    response.set_cookie("token", sign, MAX_AGE)

    return current_user

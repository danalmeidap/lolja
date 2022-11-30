from datetime import datetime, timedelta
from typing import Union

from jose import jwt

SECRET_KEY = "caa9c8f8620cbb30679026bb6427e11f"
ALGORITHM = "HS256"
EXPIRES_IN_MINUTES = 3000


def create_access_token(data: dict) -> str:
    data_for_copy = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MINUTES)

    data_for_copy.update({"exp": expiration})

    token_jwt = jwt.encode(data_for_copy, SECRET_KEY, algorithm=ALGORITHM)

    return token_jwt


def verify_access_token(token: str) -> Union[str, any]:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session
from src.infra.providers import token_provider
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.models.models import User
from src.infra.sqlalchemy.repositories.user import UserRepository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def obtain_logged_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
    )

    try:
        phonee: str = token_provider.verify_access_token(token)
    except JWTError:
        raise exception

    if not phonee:
        raise exception

    user = UserRepository(db).get_by_phone(phonee)

    if not user:
        raise exception

    return user

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.providers import hash_provider, token_provider
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.routers.utils import obtain_logged_user
from src.schemas.schemas import LoginData, LoginSucesSuccessful, User, UserOut

router = APIRouter()


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
    response_model=UserOut,
)
async def signup(user: User, db: Session = Depends(get_db)):
    user_db = UserRepository(db).get_by_phone(user.phonee)
    if user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )
    user.password = hash_provider.create_hash(user.password)
    return UserRepository(db).create(user)


@router.post(
    "/token",
    status_code=status.HTTP_200_OK,
    tags=["users"],
    response_model=LoginSucesSuccessful,
)
async def login(login: LoginData, db: Session = Depends(get_db)):
    password = login.password
    phonee = login.phonee

    exception = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="Incorrect phone or password",
    )

    user_db = UserRepository(db).get_by_phone(phonee)
    if not user_db:
        raise exception
    valid_password = hash_provider.verify_hash(password, user_db.password)
    if not valid_password:
        raise exception
    token = token_provider.create_access_token({"sub": user_db.phonee})
    return LoginSucesSuccessful(user=user_db, access_token=token)


@router.get(
    "/me",
    status_code=status.HTTP_200_OK,
    tags=["users"],
    response_model=UserOut,
)
def me(user: User = Depends(obtain_logged_user)):
    return user

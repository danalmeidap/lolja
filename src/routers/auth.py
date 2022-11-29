from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.schemas.schemas import User, UserForList, UserOut

from src.infra.providers import hash_provider


router = APIRouter()


@router.post(
    "/signup",
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
    response_model=UserOut,
)
async def signup(
    user: User, db: Session = Depends(get_db)
):
    user_db = UserRepository(db).get_by_phone(user.phonee)
    if user_db:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "User already exists")
    user.password = hash_provider.create_hash(user.password)
    return UserRepository(db).create(user)


@router.get(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    tags=["users"],
    response_model=UserOut,
)
async def get_user(
    user_id: int, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.get(
    "/user/{user_phone}",
    status_code=status.HTTP_200_OK,
    tags=["users"],
    response_model=UserOut,
)
async def get_user_by_phone(
    user_phone: str, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_by_phone(user_phone)
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="User not found")
    return user 


@router.put(
    "/user/{user_id}",
    status_code=status.HTTP_200_OK,
    tags=["users"],
    response_model=UserOut,
)
async def update_user(
    user_id: int, user: User, db: Session = Depends(get_db)
):
    if not UserRepository(db).get_user(user_id):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="User not found")
    user.password = hash_provider.create_hash(user.password)    
    UserRepository(db).update(user_id, user)  
    user = UserRepository(db).get_user(user_id)
    return user


@router.delete(
    "/users/{user_id}", status_code=status.HTTP_200_OK, tags=["users"]
)
async def delete_user(
    user_id: int, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="User not found")
    UserRepository(db).remove(user_id)
    return f"User id {user_id} deleted" 
            


from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from typing import List


class UserRepository:

    def __init__(self, db:Session) -> None:
        self.__db = db

    def create(self, user: schemas.User) ->models.User:
        db_user = models.User(name = user.name, phone = user.phone)  
        self.__db.add(db_user)
        self.__db.commit()
        self.__db.refresh(db_user)
        return db_user

    def users_list(self) ->List[models.User]:
        db_users = self.__db.query(models.User).all()
        return db_users

    def get_user(self, user_id) ->models.User:
        db_user = self.__db.query(models.User).get(user_id)   
        return db_user

    def remove(self, user_id) ->bool:
        db_user = self.__db.query(models.User).get(user_id)
        if db_user:
            self.__db.delete(db_user)
            self.__db.commit()
            return True
        return False

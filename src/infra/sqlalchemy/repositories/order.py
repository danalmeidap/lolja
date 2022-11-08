from sqlalchemy.orm import Session
from src.schemas import schemas
from typing import List
from src.infra.sqlalchemy.models import models

class OrderRepository:
    
    def __init__(self, db:Session) -> None:
        self.__db = db

    def create(self, order: schemas.Order) ->models.Order:
        db_order = models.Order(quantity = order.quantity,
                    delivery= order.delivery,
                    address= order.address,
                    observations = order.observations)
        self.__db.add(db_order)
        self.__db.commit()
        self.__db.refresh(db_order)
        return db_order

    def orders_list(self) ->List[models.Order]:
        db_orders = self.__db.query(models.Order).all()
        return db_orders

    def get_order(self, order_id:int) ->models.Order:
        db_order = self.__db.query(models.Order).get(order_id)
        return db_order

    def remove(self, order_id:int) ->bool:
        db_order= self.__db.query(models.Order).get(order_id)
        if db_order:
            self.__db.delete(db_order)
            self.__db.commit()
            return True
        return False                                
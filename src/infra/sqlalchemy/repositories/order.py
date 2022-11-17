from typing import List

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class OrderRepository:
    def __init__(self, db: Session) -> None:
        self.__db = db

    def create(self, order: schemas.Order) -> models.Order:
        db_order = models.Order(
            quantity=order.quantity,
            delivery=order.delivery,
            address=order.address,
            observations=order.observations,
            user_id=order.user_id,
            product_id=order.product_id,
        )
        self.__db.add(db_order)
        self.__db.commit()
        self.__db.refresh(db_order)
        return db_order

    def orders_list(self) -> List[models.Order]:
        db_orders = self.__db.query(models.Order).all()
        return db_orders

    def get_order(self, order_id: int) -> models.Order:
        db_order = self.__db.query(models.Order).get(order_id)
        return db_order

    def remove(self, order_id: int) -> None:
        delete_stmt = delete(models.Order).where(models.Order.id == order_id)
        self.__db.execute(delete_stmt)
        self.__db.commit()

    def update(self, order_id, order: schemas.Order) -> models.Order:
        update_stmt = (
            update(models.Order)
            .where(models.Order.id == order_id)
            .values(
                quantity=order.quantity,
                delivery=order.delivery,
                address=order.address,
                observations=order.observations,
            )
        )
        self.__db.execute(update_stmt)
        self.__db.commit()

    def get_order_by_user_id(self, user_id: int) -> List[models.Order]:
        query = select(models.Order).where(models.Order.user_id == user_id)
        orders = self.__db.execute(query).scalars().first()
        return orders

    def get_sells_by_user_id(self, user_id: int) -> List[models.Order]:
        query = (
            select(models.Order)
            .join_from(models.Order, models.Product)
            .where(models.Product.user_id == user_id)
        )
        orders = self.__db.execute(query).scalars().all()
        return orders

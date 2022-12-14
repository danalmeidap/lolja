from typing import List

from sqlalchemy import update, delete
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas


class ProductRepository:
    def __init__(self, db: Session) -> None:
        self.__db = db

    def create(self, product: schemas.Product) -> models.Product:
        db_product: models.Product = models.Product(
            name=product.name,
            details=product.details,
            price=product.price,
            avaiable=product.avaiable,
            user_id=product.user_id,
        )
        self.__db.add(db_product)
        self.__db.commit()
        self.__db.refresh(db_product)
        return db_product

    def product_list(self) -> List[models.Product]:
        db_products = self.__db.query(models.Product).all()
        return db_products

    def get_product(self, product_id) -> models.Product:
        db_product = self.__db.query(models.Product).get(product_id)
        return db_product

    def update(self, product_id, product: schemas.Product):
        update_stmt = (
            update(models.Product)
            .where(models.Product.id == product_id)
            .values(
                name=product.name,
                details=product.details,
                price=product.price,
                avaiable=product.avaiable,
            )
        )
        self.__db.execute(update_stmt)
        self.__db.commit()

    def remove(self, product_id) -> None:
        delete_stmt= delete(models.Product).where(models.Product == product_id)
        self.__db.execute(delete_stmt)
        self.__db.commit()
from typing import List

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
            user_id= product.user_id

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

    def remove(self, product_id) -> bool:
        db_product = self.__db.query(models.Product).get(product_id)
        if db_product:
            self.__db.delete(db_product)
            self.__db.commit()
            return True
        return False

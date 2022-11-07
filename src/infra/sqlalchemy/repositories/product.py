from sqlalchemy.orm import Session
from typing import List
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class ProductRepository:
    
    def __init__(self, db:Session) -> None:
        self.__db = db
         
    def create(self, product: schemas.Product) ->models.Product:
        db_product: models.Product = models.Product(name= product.name,
                        details= product.details,
                        price= product.price,
                        avaiable= product.avaiable)
        self.__db.add(db_product)
        self.__db.commit()
        self.__db.refresh(db_product)
        return db_product                

    def product_list(self) ->List[models.Product]:
        products = self.__db.query(models.Product).all()
        return products

    def get_product(self, product_id):
        product = self.__db.query(models.Product).filter(product_id).one()
        return product

    def remove(self):
        pass    
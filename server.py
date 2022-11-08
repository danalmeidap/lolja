from fastapi import FastAPI, Depends
from src.schemas.schemas import Product
from src.infra.sqlalchemy.repositories.product import ProductRepository
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, create_db

app = FastAPI()
create_db()

@app.get("/products")
def products_list():
    
    return {"Message": "Products List"}

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = ProductRepository(db).create(product)
    return {"Message": product}

from fastapi import FastAPI, Depends
from src.schemas.schemas import Product
from src.schemas.schemas import User
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.infra.sqlalchemy.repositories.user import UserRepository
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db, create_db

app = FastAPI()
create_db()

@app.get("/products")
def products_list(db:Session=Depends(get_db)):
    products = ProductRepository(db).product_list()
    return products

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    created_product = ProductRepository(db).create(product)
    return created_product

@app.get("/products/{product_id}")
def get_product(product_id:int, db: Session = Depends(get_db)):
    product = ProductRepository(db).get_product(product_id)
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id:int, db:Session = Depends(get_db)):
    deleted_product = ProductRepository(db).remove(product_id)
    if deleted_product:
        return {"Msg": "Product Deleted"}
    return {"Msg":"You don't have products with this id"}    

@app.get("/users")
def users_list(db:Session=Depends(get_db)):
    users = UserRepository(db).users_list()
    return users

@app.post("/users")
def create_user(user: User, db:Session= Depends(get_db)):
    created_user = UserRepository(db).create(user)
    return created_user

@app.get("/users/{user_id}")
def get_user(user_id:int, db:Session= Depends(get_db)):
    user = UserRepository(db).get_user(user_id)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id:int, db:Session= Depends(get_db)):
    deleted_user= UserRepository(db).remove(user_id)
    if deleted_user:
        return {"msg": "User deleted"}
    return {"msg":"You don't have users with this id"}    

from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.order import OrderRepository
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.schemas.schemas import Order, Product, User

app = FastAPI()
create_db()


@app.get("/products")
async def products_list(response: Response, db: Session = Depends(get_db)):
    products = ProductRepository(db).product_list()
    return products


@app.post("/products")
async def create_product(
    product: Product, response: Response, db: Session = Depends(get_db)
):
    created_product = ProductRepository(db).create(product)
    response.status_code = status.HTTP_201_CREATED
    return created_product


@app.get("/products/{product_id}")
async def get_product(
    product_id: int, response: Response, db: Session = Depends(get_db)
):
    product = ProductRepository(db).get_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
    return product if product else response


@app.delete("/products/{product_id}")
async def delete_product(
    product_id: int, response: Response, db: Session = Depends(get_db)
):
    product = ProductRepository(db).get_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if ProductRepository(db).remove(product_id):
            response.status_code = status.HTTP_204_NO_CONTENT
        return (
            f"Product id {product_id} deleted"
            if response.status_code == status.HTTP_204_NO_CONTENT
            else response
        )


@app.get("/users")
async def users_list(db: Session = Depends(get_db)):
    users = UserRepository(db).users_list()
    return users


@app.post("/users")
async def create_user(user: User, response: Response, db: Session = Depends(get_db)):
    created_user = UserRepository(db).create(user)
    response.status_code = status.HTTP_201_CREATED
    return created_user


@app.get("/users/{user_id}")
async def get_user(user_id: int, response: Response, db: Session = Depends(get_db)):
    user = UserRepository(db).get_user(user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    return user if user else response


@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int, response: Response, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user(user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if UserRepository(db).remove(user_id):
            response.status_code = status.HTTP_204_NO_CONTENT
        return (
            f"User id {user_id} deleted"
            if response.status_code == status.HTTP_204_NO_CONTENT
            else response
        )


@app.get("/orders")
async def orders_list(db: Session = Depends(get_db)):
    return OrderRepository(db).orders_list()


@app.post("/orders")
async def create_order(
    order: Order, response: Response, db: Session = Depends(get_db)
):
    created_order = OrderRepository(db).create(order)
    response.status_code = status.HTTP_201_CREATED
    return created_order


@app.get("/orders/{order_id}")
async def get_order(
    order_id: int, response: Response, db: Session = Depends(get_db)
):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        response.status_code = status.HTTP_404_NOT_FOUND
    return order if order else response


@app.delete("/orders/{user_id}")
async def delete_order(
    order_id: int, response: Response, db: Session = Depends(get_db)
):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if OrderRepository.remove(order_id):
            response.status_code = status.HTTP_204_NO_CONTENT
        return (
            f"Order id {order_id} deleted"
            if response.status_code == status.HTTP_204_NO_CONTENT
            else response
        )

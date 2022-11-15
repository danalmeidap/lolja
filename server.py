from enum import Enum
from typing import List

from fastapi import Depends, FastAPI, Response, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.order import OrderRepository
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.infra.sqlalchemy.repositories.user import UserRepository
from src.schemas.schemas import Order, OrderOut, Product, ProductOut, User, UserOut

app = FastAPI()
create_db()


class Tags(Enum):
    products = "products"
    users = "users"
    orders = "orders"


@app.get(
    "/products",
    status_code=status.HTTP_200_OK,
    tags=[Tags.products],
    response_model=List[ProductOut],
)
async def products_list(response: Response, db: Session = Depends(get_db)):
    return ProductRepository(db).product_list()


@app.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.products],
    response_model=ProductOut,
)
async def create_product(
    product: Product, response: Response, db: Session = Depends(get_db)
):
    response.status_code = status.HTTP_201_CREATED
    return ProductRepository(db).create(product)


@app.get(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.products],
    response_model=ProductOut,
)
async def get_product(
    product_id: int, response: Response, db: Session = Depends(get_db)
):
    product = ProductRepository(db).get_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
    return product if product else response


@app.put(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.products],
    response_model=ProductOut,
)
async def update_product(
    product_id: int,
    response: Response,
    product: Product,
    db: Session = Depends(get_db),
):
    if not ProductRepository(db).get_product(product_id):
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        ProductRepository(db).update(product_id, product)
        response.status_code = status.HTTP_200_OK
    product = ProductRepository(db).get_product(product_id)
    return product if product else response


@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.products],
)
async def delete_product(
    product_id: int, response: Response, db: Session = Depends(get_db)
):
    product = ProductRepository(db).get_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if ProductRepository(db).remove(product_id):
            response.status_code = status.HTTP_200_OK
        return (
            f"Product id {product_id} deleted"
            if response.status_code == status.HTTP_200_OK
            else response
        )


@app.get(
    "/users",
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    response_model=List[UserOut],
)
async def users_list(db: Session = Depends(get_db)):
    return UserRepository(db).users_list()


@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.users],
    response_model=UserOut,
)
async def create_user(
    user: User, response: Response, db: Session = Depends(get_db)
):
    response.status_code = status.HTTP_201_CREATED
    return UserRepository(db).create(user)


@app.get(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    response_model=UserOut,
)
async def get_user(
    user_id: int, response: Response, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user(user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    return user if user else response


@app.get(
    "/user/{user_phone}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    response_model=UserOut,
)
async def get_user_by_phone(
    user_phone: str, response: Response, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_by_phone(user_phone)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    return user if user else response


@app.put(
    "/user/{user_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.users],
    response_model=UserOut,
)
async def update_user(
    user_id: int, response: Response, user: User, db: Session = Depends(get_db)
):
    if not UserRepository(db).get_user(user_id):
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        UserRepository(db).update(user_id, user)
        response.status_code = status.HTTP_200_OK
    user = UserRepository(db).get_user(user_id)
    return user if user else response


@app.delete(
    "/users/{user_id}", status_code=status.HTTP_200_OK, tags=[Tags.users]
)
async def delete_user(
    user_id: int, response: Response, db: Session = Depends(get_db)
):
    user = UserRepository(db).get_user(user_id)
    if not user:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if UserRepository(db).remove(user_id):
            response.status_code = status.HTTP_200_OK
        return (
            f"User id {user_id} deleted"
            if response.status_code == status.HTTP_200_OK
            else response
        )


@app.get(
    "/orders",
    status_code=status.HTTP_200_OK,
    tags=[Tags.orders],
    response_model=List[OrderOut],
)
async def orders_list(db: Session = Depends(get_db)):
    return OrderRepository(db).orders_list()


@app.post(
    "/orders",
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.orders],
    response_model=OrderOut,
)
async def create_order(
    order: Order, response: Response, db: Session = Depends(get_db)
):
    response.status_code = status.HTTP_201_CREATED
    return OrderRepository(db).create(order)


@app.get(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.orders],
    response_model=OrderOut,
)
async def get_order(
    order_id: int, response: Response, db: Session = Depends(get_db)
):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        response.status_code = status.HTTP_404_NOT_FOUND
    return order if order else response


@app.put(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    tags=[Tags.orders],
    response_model=OrderOut,
)
async def update_order(
    order_id: int,
    response: Response,
    order: Order,
    db: Session = Depends(get_db),
):
    if not OrderRepository(db).get_order(order_id):
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        OrderRepository(db).update(order_id, order)
        response.status_code = status.HTTP_200_OK
    order = OrderRepository(db).get_order(order_id)
    return order if order else response


@app.delete(
    "/orders/{order_id}", status_code=status.HTTP_200_OK, tags=[Tags.orders]
)
async def delete_order(
    order_id: int, response: Response, db: Session = Depends(get_db)
):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        response.status_code = status.HTTP_404_NOT_FOUND
    else:
        if OrderRepository(db).remove(order_id):
            response.status_code = status.HTTP_200_OK
        return (
            f"Order id {order_id} deleted"
            if response.status_code == status.HTTP_200_OK
            else response
        )

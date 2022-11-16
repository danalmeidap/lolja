from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.order import OrderRepository
from src.schemas.schemas import Order, OrderOut

router = APIRouter()


@router.get(
    "/orders",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
    response_model=List[OrderOut],
)
async def orders_list(db: Session = Depends(get_db)):
    return OrderRepository(db).orders_list()


@router.post(
    "/orders",
    status_code=status.HTTP_201_CREATED,
    tags=["orders"],
    response_model=OrderOut,
)
async def create_order(
    order: Order, response: Response, db: Session = Depends(get_db)
):
    response.status_code = status.HTTP_201_CREATED
    return OrderRepository(db).create(order)


@router.get(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
    response_model=OrderOut,
)
async def get_order(
    order_id: int, response: Response, db: Session = Depends(get_db)
):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        response.status_code = status.HTTP_404_NOT_FOUND
    return order if order else response


@router.put(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
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


@router.delete(
    "/orders/{order_id}", status_code=status.HTTP_200_OK, tags=["orders"]
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

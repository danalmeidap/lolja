from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
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
async def create_order(order: Order, db: Session = Depends(get_db)):
    return OrderRepository(db).create(order)


@router.get(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
    response_model=OrderOut,
)
async def get_order(order_id: int, db: Session = Depends(get_db)):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    return order


@router.get(
    "/orders/{user_id}",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
    response_model=OrderOut,
)
async def get_order_by_user_id(user_id: int, db: Session = Depends(get_db)):
    orders = OrderRepository(db).get_orders_by_user_id(user_id)
    if not orders:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    return orders


@router.get(
    "/orders{user_id}",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
    response_model=List[OrderOut],
)
def get_sells_by_user_id(user_id: int, db: Session = Depends(get_db)):
    order = OrderRepository(db).get_sells_by_user_id(user_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    return order


@router.put(
    "/orders/{order_id}",
    status_code=status.HTTP_200_OK,
    tags=["orders"],
    response_model=OrderOut,
)
async def update_order(
    order_id: int,
    order: Order,
    db: Session = Depends(get_db),
):
    if not OrderRepository(db).get_order(order_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    OrderRepository(db).update(order_id, order)
    order = OrderRepository(db).get_order(order_id)
    return order


@router.delete(
    "/orders/{order_id}", status_code=status.HTTP_200_OK, tags=["orders"]
)
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = OrderRepository(db).get_order(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Order not found"
        )
    OrderRepository(db).remove(order_id)
    return f"Order id {order_id} deleted"

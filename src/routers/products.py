from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.product import ProductRepository
from src.schemas.schemas import Product, ProductOut

router = APIRouter()


@router.get(
    "/products",
    status_code=status.HTTP_200_OK,
    tags=["products"],
    response_model=List[Product],
)
async def products_list(response: Response, db: Session = Depends(get_db)):
    return ProductRepository(db).product_list()


@router.post(
    "/products",
    status_code=status.HTTP_201_CREATED,
    tags=["products"],
    response_model=ProductOut,
)
async def create_product(
    product: Product, response: Response, db: Session = Depends(get_db)
):
    response.status_code = status.HTTP_201_CREATED
    return ProductRepository(db).create(product)


@router.get(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    tags=["products"],
    response_model=ProductOut,
)
async def get_product(
    product_id: int, response: Response, db: Session = Depends(get_db)
):
    product = ProductRepository(db).get_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
    return product if product else response


@router.put(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK,
    tags=["products"],
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


@router.delete(
    "/products/{product_id}", status_code=status.HTTP_200_OK, tags=["products"]
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

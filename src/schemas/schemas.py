from typing import List, Optional

from pydantic import BaseModel


class ProductOut(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    avaiable: bool

    class Config:
        orm_mode = True


class User(BaseModel):
    id: Optional[int] = None
    name: str
    phonee: str
    password: str
    products: List[ProductOut] = []

    class Config:
        orm_mode = True


class UserForList(BaseModel):
    id: Optional[int] = None
    name: str
    phonee: str
    products: List[ProductOut] = []

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: Optional[int] = None
    name: str
    phonee: str

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    details: str
    price: float
    avaiable: bool = False
    user_id: Optional[int]
    user: Optional[UserOut]

    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[int] = None
    quantity: int
    delivery: bool = True
    address: str
    observations: Optional[str] = "No observations"
    user_id: Optional[int]
    product_id: Optional[int]

    class Config:
        orm_mode = True


class OrderOut(BaseModel):
    id: Optional[int] = None
    quantity: int
    address: str
    observations: str
    user: Optional[UserOut]
    product: Optional[ProductOut]

    class Config:
        orm_mode = True

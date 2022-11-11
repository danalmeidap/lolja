from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: Optional[str] = None
    name: str


    class Config:
        orm_mode= True


class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    avaiable: bool = False

    class Config:
        orm_mode = True


class ProductOut(BaseModel):
    id: Optional[str] = None
    name: str
    price: float

    class Config:
        orm_mode = True       


class Order(BaseModel):
    id: Optional[str] = None
    quantity: int
    delivery: bool = True
    address: str
    observations: Optional[str] = "No observations"

    class Config:
        orm_mode = True


class OrderOut(BaseModel):
    id: Optional[str] = None
    quantity: int
    address: str

    class Config:
        orm_mode = True
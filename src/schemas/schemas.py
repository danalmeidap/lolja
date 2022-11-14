from typing import Optional, List

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[str] = None
    name: str
    phonee: str
    password: str


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
    user_id:int
    
    class Config:
        orm_mode = True


class ProductOut(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    user:User
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
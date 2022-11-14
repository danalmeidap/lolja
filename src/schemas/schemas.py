from typing import Optional, List

from pydantic import BaseModel


class User(BaseModel):
    id: Optional[int] = None
    name: str
    phonee: str
    password: str
    

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    id: Optional[int] = None
    name: str
    phonee: str
    
    
    class Config:
        orm_mode= True

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    details: str
    price: float
    avaiable: bool = False
    user_id:Optional[int]
    user: Optional[UserOut]

    class Config:
        orm_mode = True

class ProductOut(BaseModel):
    id: Optional[str] = None
    name: str
    price: float


    class Config:
        orm_mode = True


class Order(BaseModel):
    id: Optional[int] = None
    quantity: int
    delivery: bool = True
    address: str
    observations: Optional[str] = "No observations"
    user_id:Optional[int]
    product_id:Optional[int]
    

    class Config:
        orm_mode = True
class OrderOut(BaseModel):
    id: Optional[str] = None
    quantity: int
    address: str
    user: Optional[UserOut]
    product:Optional[ProductOut]

    
    class Config:
        orm_mode = True
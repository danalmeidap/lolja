from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str



class Product(BaseModel):
    id: Optional[str] = None
    name: str
    details: str
    price: float
    avaiable: bool = False

    class config:
        orm_mode = True

class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delivery: bool = True
    address: str
    observations: Optional[str]= "No observations"


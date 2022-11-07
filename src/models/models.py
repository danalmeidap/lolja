from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    id: Optional[str] = None
    name: str
    phone: str
    products: List[Product]
    sales: List[Order]
    ordered: List[Order]


class Product(BaseModel):
    id: Optional[str] = None
    user:User
    name: str
    details: str
    price: float
    avaiable: bool = False

class Order(BaseModel):
    id: Optional[str] = None
    user: User
    product: Product
    quantity: int
    delivery: bool = True
    address: str
    observations: Optional[str]= "No observations"


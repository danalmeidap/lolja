from sqlalchemy import Column, String, Integer,Float, Boolean
from src.infra.sqlalchemy.config.database import Base 

class Product(Base):

    __tablename__ = "product"

    id= Column(Integer, primary_key= True, index= True)
    name= Column(String)
    details= Column(String)
    price= Column(Float)
    avaiable= Column(Boolean)



from sqlalchemy import Column, String, Integer,Float, Boolean
from src.infra.sqlalchemy.config.database import Base 

class Product(Base):

    __tablename__ = "product"

    id= Column(Integer, primary_key= True, index= True)
    name= Column(String)
    details= Column(String)
    price= Column(Float)
    avaiable= Column(Boolean)


class User(Base):
    
    __tablename__ = "user"

    id= Column(Integer, primary_key= True, index= True)
    name= Column(String)
    phone= Column(String)


class Order(Base):

    __tablename__ = "order"

    id= Column(Integer, primary_key= True, index=True)
    quantity= Column(Integer)
    delivery= Column(Boolean)
    address= Column(String)
    observations= Column(String) 
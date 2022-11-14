from sqlalchemy import Boolean, Column, Float, Integer, String,ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    avaiable = Column(Boolean)
    user_id = Column(Integer, ForeignKey('user.id', name='fk_user'))

    user= relationship('User', back_populates= 'products') 


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phonee = Column(String)
    password = Column(String)
    

    products = relationship('Product', back_populates='user')
    
       


class Order(Base):

    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)
    delivery = Column(Boolean)
    address = Column(String)
    observations = Column(String)

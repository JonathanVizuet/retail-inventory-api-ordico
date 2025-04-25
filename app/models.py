from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    discount = Column(Float, nullable=True)
    discount_price = Column(Float, nullable=True)


class ProductReturn(Base):
    __tablename__ = "product_returns"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    reason = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)

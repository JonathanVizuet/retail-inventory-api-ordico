from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int
    discount: Optional[float] = None
    discount_price: Optional[float] = None


class ProductRead(ProductCreate):
    id: int

    model_config = {"from_attributes": True}

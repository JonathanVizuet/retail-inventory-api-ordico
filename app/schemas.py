from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int


class ProductRead(ProductCreate):
    id: int

    model_config = {"from_attributes": True}

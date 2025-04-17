from sqlalchemy.orm import Session
from app.models import Product
from app.schemas import ProductCreate

class ProductService:
    @staticmethod
    def create_product(db: Session, product_data: ProductCreate) -> Product:
        new_product = Product(**product_data.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
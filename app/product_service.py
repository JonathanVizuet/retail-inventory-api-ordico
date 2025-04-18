from fastapi import HTTPException
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

    @staticmethod
    def get_product(db: Session, product_id: int) -> Product:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="No se encontró el producto")
        return product

    @staticmethod
    def update_stock(db: Session, product_id: int, nuevo_stock: int) -> Product:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="No se encontró el producto a actualizar")
        product.stock = nuevo_stock
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete_product(db: Session, product_id: int) -> bool:
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return False
        db.delete(product)
        db.commit()
        return True
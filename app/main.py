from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ProductCreate, ProductRead
from app.product_service import ProductService

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/products", response_model=ProductRead)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, product)
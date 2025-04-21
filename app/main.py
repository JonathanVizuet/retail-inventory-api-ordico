from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

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


@app.get("/products/{product_id}", response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductService.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return product


@app.put("/products/{product_id}", response_model=ProductRead)
def update_product_stock(product_id: int, stock: int, db: Session = Depends(get_db)):
    updated_product = ProductService.update_stock(db, product_id, stock)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return updated_product


@app.delete("/products/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    success = ProductService.delete_product(db, product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return JSONResponse(content={"detail": "Producto eliminado correctamente"})


@app.put("/products/{product_id}/apply-discount", response_model=ProductRead)
def discount(product_id: int, discount: float, db: Session = Depends(get_db)):
    update_product_discount = ProductService.apply_discount(db, product_id, discount)
    if not update_product_discount:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return update_product_discount

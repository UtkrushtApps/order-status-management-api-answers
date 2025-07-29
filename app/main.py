from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Status Management API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.put("/orders/{order_id}/status", response_model=schemas.OrderResponse)
def update_order_status(order_id: int, order_update: schemas.OrderUpdate, db: Session = Depends(get_db)):
    """Update the status of an existing order."""
    updated_order = crud.update_order_status(db, order_id, order_update.status)
    return updated_order

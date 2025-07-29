from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException, status

def get_order(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def update_order_status(db: Session, order_id: int, new_status: schemas.OrderStatusEnum):
    order = get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order.status = new_status
    db.commit()
    db.refresh(order)
    return order

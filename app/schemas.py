from pydantic import BaseModel
from enum import Enum

class OrderStatusEnum(str, Enum):
    pending = 'pending'
    shipped = 'shipped'
    delivered = 'delivered'
    cancelled = 'cancelled'

class OrderUpdate(BaseModel):
    status: OrderStatusEnum

class OrderResponse(BaseModel):
    id: int
    status: OrderStatusEnum

    class Config:
        orm_mode = True

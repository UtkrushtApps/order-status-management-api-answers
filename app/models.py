from sqlalchemy import Column, Integer, String, Enum as SqlEnum
from .database import Base
import enum

class OrderStatusEnum(str, enum.Enum):
    pending = 'pending'
    shipped = 'shipped'
    delivered = 'delivered'
    cancelled = 'cancelled'

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    status = Column(SqlEnum(OrderStatusEnum, name="orderstatusenum", create_constraint=True), nullable=False, default=OrderStatusEnum.pending)

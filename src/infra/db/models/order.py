import enum

import sqlalchemy as sa
from sqlalchemy import Column, Enum
from sqlalchemy.orm import relationship

from src.infra.db.models.common import Base

from sqlalchemy.dialects import postgresql as psql

class OrderStatus(str, enum.Enum):
    in_process = "in_process"
    shipped = "completed"
    delivered = "cancelled"


class Order(Base):
    __tablename__ = 'orders'

    status = Column(Enum(OrderStatus), default=OrderStatus.in_process, nullable=False)

    items = relationship("OrderItem", back_populates="order")

    def __repr__(self):
        return f"<Order(id={self.id}, created_at={self.created_at}, status={self.status})>"

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = sa.Column(psql.UUID(as_uuid=True), sa.ForeignKey('orders.id'), nullable=False)
    product_id = sa.Column(psql.UUID(as_uuid=True), sa.ForeignKey('products.id'), nullable=False)
    quantity = sa.Column(sa.Integer, nullable=False)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")


    def __repr__(self):
        return f"<OrderItem(id={self.id}, order_id={self.order_id}, product_id={self.product_id}, quantity={self.quantity})>"

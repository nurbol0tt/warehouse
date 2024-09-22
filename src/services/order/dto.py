from pydantic import BaseModel, UUID4

from src.infra.db.models.order import OrderStatus


class Order(BaseModel):
    quantity: int
    product_id: UUID4


class OrderUpdateStatus(BaseModel):
    status: OrderStatus

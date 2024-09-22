from typing import Protocol, List

from pydantic import UUID4

from src.infra.db.models.order import Order, OrderItem
from src.services.order import dto


class IOrderRepository(Protocol):

    async def create(self, order: Order) -> Order:
        ...

    async def create_order_item(self, order_item: OrderItem) -> OrderItem:
        ...

    async def get_order_by_id(self, order_id: UUID4) -> Order:
        ...

    async def update(self, order_id: UUID4, dto: dto.OrderUpdateStatus) -> Order:
        ...

    async def get_all_orders(self) -> List[Order]:
        ...

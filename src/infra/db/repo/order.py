from typing import List

from pydantic import UUID4
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.infra.db.models.order import OrderItem, Order
from src.infra.db.repo.common import SQLAlchemyRepo
from src.interfaces.repositories.alchemy.order import IOrderRepository
from src.services.order import dto



class OrderRepository(SQLAlchemyRepo, IOrderRepository):

    async def create(self, order: Order) -> Order:
        self.session.add(order)
        await self.session.commit()
        return order

    async def create_order_item(self, order_item: OrderItem) -> OrderItem:
        self.session.add(order_item)
        await self.session.commit()
        return order_item

    async def get_order_by_id(self, order_id: UUID4) -> Order:
        query = select(Order).options(selectinload(Order.items)).where(Order.id == order_id)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def update(self, order_id: UUID4, dto: dto.OrderUpdateStatus) -> Order:
        order = await self.get_order_by_id(order_id=order_id)
        order.status = dto.status
        await self.session.commit()
        return order

    async def get_all_orders(self) -> List[Order]:
        query = select(Order)
        result = await self.session.execute(query)
        return result.scalars().all()

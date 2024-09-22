from pydantic import UUID4

from src.infra.db.models.order import Order, OrderItem
from src.interfaces.db import get_session
from src.interfaces.repositories.alchemy.order import IOrderRepository
from src.interfaces.repositories.alchemy.product import IProductRepository
from src.services.order import dto
from src.services.order.exceptions import OrderNotFound
from src.services.product.exceptions import InsufficientQuantityStock


class CreateOrderService:
    def __init__(
            self,
            session: get_session,
            repo: IOrderRepository,
            product_repo: IProductRepository,  # Репозиторий для работы с продуктами

    ) -> None:
        self.session = session
        self.repo = repo
        self.product_repo = product_repo

    async def __call__(self, dto: dto.Order):
        product = await self.product_repo.get_product_by_id(product_id=dto.product_id)
        print(product)
        print(product.total)
        if product.total < dto.quantity:
            raise InsufficientQuantityStock

        order = Order()
        order = await self.repo.create(order=order)

        order_item = OrderItem(
            order_id=order.id,
            quantity=dto.quantity,
            product_id=dto.product_id,
        )
        await self.repo.create_order_item(order_item=order_item)
        product.total -= dto.quantity
        await self.session.commit()

        return order

class GetAllOrderService:
    def __init__(
            self,
            session: get_session,
            repo: IOrderRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self):
        return await self.repo.get_all_orders()



class GetOrderService:
    def __init__(
            self,
            session: get_session,
            repo: IOrderRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self, order_id: UUID4) -> Order:
        return await self.repo.get_order_by_id(order_id=order_id)


class UpdateOrderService:
    def __init__(
            self,
            session: get_session,
            repo: IOrderRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self, id: UUID4, dto: dto.Order) -> Order:
        if not (
            await self.repo.get_order_by_id(order_id=id)
        ):
            raise OrderNotFound
        return await self.repo.update(order_id=id, dto=dto)

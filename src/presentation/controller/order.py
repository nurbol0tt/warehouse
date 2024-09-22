from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import (
    APIRouter,
)
from pydantic import UUID4
from src.services.order import dto

from src.services.order.services import (
    CreateOrderService,
    GetOrderService,
    GetAllOrderService,
    UpdateOrderService,
)

order_router = APIRouter(prefix='/orders', tags=['orders'],  route_class=DishkaRoute)


@order_router.post("/")
async def create_order(dto: dto.Order, service: FromDishka[CreateOrderService]):
    return await service(dto=dto)


@order_router.get("/{order_id}")
async def get_order(order_id: UUID4, service: FromDishka[GetOrderService]):
    return await service(order_id=order_id)


@order_router.get("/")
async def get_orders(service: FromDishka[GetAllOrderService]):
    return await service()


@order_router.patch("/{id}/status")
async def update_products(id: UUID4, dto: dto.OrderUpdateStatus, service: FromDishka[UpdateOrderService]):
    return await service(id=id, dto=dto)

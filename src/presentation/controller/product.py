from dishka import FromDishka
from dishka.integrations.fastapi import DishkaRoute
from fastapi import (
    APIRouter,
)
from pydantic import UUID4

from src.services.product import dto
from src.services.product.services import (
    CreateProductService,
    GetProductService,
    GetAllProductService,
    UpdateProductService,
    DeleteProductService,
)

product_router = APIRouter(prefix='/products', tags=['products'], route_class=DishkaRoute)


@product_router.post("/")
async def create_product(dto: dto.Product, service: FromDishka[CreateProductService]):
    return await service(dto=dto)


@product_router.get("/{product_id}")
async def get_product(product_id: UUID4, service: FromDishka[GetProductService]):
    return await service(product_id=product_id)


@product_router.get("/")
async def get_products(service: FromDishka[GetAllProductService]):
    return await service()


@product_router.patch("/{product_id}")
async def update_products(product_id: UUID4, dto: dto.Product, service: FromDishka[UpdateProductService]):
    return await service(product_id=product_id, dto=dto)


@product_router.delete("/{product_id}")
async def delete_products(product_id: UUID4, service: FromDishka[DeleteProductService]):
    return await service(product_id=product_id)


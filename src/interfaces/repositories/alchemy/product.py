from typing import Protocol, List

from pydantic import UUID4

from src.infra.db.models.product import Product
from src.services.product import dto


class IProductRepository(Protocol):
    async def create(self, product: Product) -> Product:
        ...

    async def get_product_by_id(self, product_id: UUID4) -> Product:
        ...

    async def delete(self, product_id: UUID4) -> None:
        ...

    async def update(self, product_id: UUID4, dto: dto.Product) -> Product:
        ...

    async def get_all_products(self) -> List[Product]:
        ...

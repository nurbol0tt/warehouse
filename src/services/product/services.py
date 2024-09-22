from typing import List

from pydantic.v1 import UUID4

from src.infra.db.models.product import Product
from src.interfaces.db import get_session
from src.interfaces.repositories.alchemy.product import IProductRepository
from src.services.product import dto
from src.services.product.exceptions import ProductNotFound


class CreateProductService:
    def __init__(
            self,
            session: get_session,
            repo: IProductRepository,
    ):
        self.session = session
        self.repo = repo

    async def __call__(self, dto: dto.Product) -> dto.Product:
        product = (
                Product(
                    title=dto.title,
                    description=dto.description,
                    price=dto.price,
                    total=dto.total
                )
        )
        return await self.repo.create(product=product)


class GetAllProductService:
    def __init__(
            self,
            session: get_session,
            repo: IProductRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self) -> List[dto.Product]:
        return await self.repo.get_all_products()



class GetProductService:
    def __init__(
            self,
            session: get_session,
            repo: IProductRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self, product_id: UUID4) -> dto.Product:
        return await self.repo.get_product_by_id(product_id=product_id)


class UpdateProductService:
    def __init__(
            self,
            session: get_session,
            repo: IProductRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self, product_id: UUID4, dto: dto.Product) -> dto.Product:
        if not (
            await self.repo.get_product_by_id(product_id=product_id)
        ):
            raise ProductNotFound
        return await self.repo.update(product_id=product_id, dto=dto)


class DeleteProductService:
    def __init__(
            self,
            session: get_session,
            repo: IProductRepository,
    ) -> None:
        self.session = session
        self.repo = repo

    async def __call__(self, product_id: UUID4) -> None:
        if not (
                await self.repo.get_product_by_id(product_id=product_id)
        ):
            raise ProductNotFound
        return await self.repo.delete(product_id=product_id)



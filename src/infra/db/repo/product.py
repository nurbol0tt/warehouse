from typing import List

from pydantic import UUID4
from sqlalchemy import select, update

from src.infra.db.models.product import Product
from src.infra.db.repo.common import SQLAlchemyRepo
from src.interfaces.repositories.alchemy.product import IProductRepository
from src.services.product import dto



class ProductRepository(SQLAlchemyRepo, IProductRepository):

    async def create(self, product: Product) -> Product:
        self.session.add(product)
        await self.session.commit()
        return product

    async def get_product_by_id(self, product_id: UUID4) -> Product:
        query = select(Product).where(Product.id == product_id)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()

    async def delete(self, product_id: UUID4) -> None:
        blog = await self.get_product_by_id(product_id=product_id)
        await self.session.delete(blog)
        await self.session.commit()

    async def update(self, product_id: UUID4, dto: dto.Product) -> Product:
        product = await self.session.get(Product, product_id)
        for field, value in dto.dict().items():
            setattr(product, field, value)

        await self.session.commit()
        return product

    async def get_all_products(self) -> List[Product]:
        query = select(Product)
        result = await self.session.execute(query)
        return result.scalars().all()

from dishka import Provider, provide

from src.infra.db.repo.order import OrderRepository
from src.infra.db.repo.product import ProductRepository
from src.interfaces.repositories.alchemy.order import IOrderRepository
from src.interfaces.repositories.alchemy.product import IProductRepository


class RepositoryProvider(Provider):
    product_repository = provide(ProductRepository, provides=IProductRepository)
    order_repository = provide(OrderRepository, provides=IOrderRepository)
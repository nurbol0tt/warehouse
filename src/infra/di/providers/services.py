from dishka import Provider, provide

from src.services.order.services import CreateOrderService, GetOrderService, GetAllOrderService, UpdateOrderService
from src.services.product.services import (
    CreateProductService,
    GetProductService,
    GetAllProductService,
    UpdateProductService,
    DeleteProductService,
)


class ServiceProvider(Provider):
    product_service = provide(CreateProductService)
    get_all_product_service = provide(GetAllProductService)
    get_product_service = provide(GetProductService)
    update_product_service = provide(UpdateProductService)
    delete_product_service = provide(DeleteProductService)

    order_service = provide(CreateOrderService)
    get_order_service = provide(GetOrderService)
    get_orders_service = provide(GetAllOrderService)
    update_orders_service = provide(UpdateOrderService)
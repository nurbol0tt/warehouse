from fastapi import APIRouter

from src.presentation.controller.order import order_router
from src.presentation.controller.product import product_router


def bind_routes():
    router = APIRouter(prefix='/api')
    router.include_router(product_router)
    router.include_router(order_router)
    return router


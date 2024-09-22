from fastapi import FastAPI

from src.presentation.exceptions.handler import (
    not_found_error_handler,
    logic_error_handler,
)

from src.services.product.exceptions import (
    ProductNotFound,
    NoBalanceError, InsufficientQuantityStock,
)


def register_exceptions(app: FastAPI) -> None:
    app.exception_handlers.setdefault(
        ProductNotFound, not_found_error_handler,
    )
    app.exception_handlers.setdefault(
        InsufficientQuantityStock, logic_error_handler,
    )
    app.exception_handlers.setdefault(
        ValueError, logic_error_handler,
    )
from dishka.integrations.starlette import setup_dishka
from fastapi import FastAPI

from src.infra.di.container import get_container
from src.presentation.controller.register import bind_routes
from src.presentation.exceptions.register import register_exceptions


def initialize_app(_app: FastAPI) -> FastAPI:
    _app.include_router(bind_routes())
    register_exceptions(_app)
    container = get_container()
    setup_dishka(container, _app)
    return _app


app = initialize_app(
    FastAPI(),
)
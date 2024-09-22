from dishka import AsyncContainer, Scope, make_async_container

from src.infra.di.providers.repositories import RepositoryProvider
from src.infra.di.providers.services import ServiceProvider
from src.infra.di.providers.sesssion import SessionProvider


def get_container() -> AsyncContainer:
    repository_provider = RepositoryProvider(scope=Scope.REQUEST)
    service_provider = ServiceProvider(scope=Scope.REQUEST)
    session_provider = SessionProvider(scope=Scope.SESSION)

    return make_async_container(
        service_provider,
        repository_provider,
        session_provider,
    )
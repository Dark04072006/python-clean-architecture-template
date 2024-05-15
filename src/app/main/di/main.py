from dishka import AsyncContainer, make_async_container

from app.main.di.providers.adapters import SqlalchemyProvider


def container_factory() -> AsyncContainer:
    return make_async_container(SqlalchemyProvider())

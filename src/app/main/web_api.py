from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI

from app.main.di.main import container_factory
from app.presentation.web_api.exc_handlers import init_exception_handlers
from app.presentation.web_api.routers import health_check_router


def init_di(app: FastAPI) -> None:
    container = container_factory()

    setup_dishka(container, app)


def init_routers(app: FastAPI) -> None:
    app.include_router(health_check_router)


def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)
    init_routers(app)
    init_exception_handlers(app)

    return app

from functools import partial

from dishka.integrations.fastapi import DishkaRoute, setup_dishka
from fastapi import APIRouter, FastAPI

from app.main.di.main import container_factory
from app.presentation.web_api.exc_handlers import init_exception_handlers
from app.presentation.web_api.routers import health_check_router


def init_di(app: FastAPI, autoinject: bool = True) -> None:
    def include_router_autoinject(app_: FastAPI, router: APIRouter, **kwargs) -> None:
        setattr(router, "route_class", DishkaRoute)
        app_.router.include_router(router, **kwargs)

    if autoinject:
        setattr(app, "include_router", partial(include_router_autoinject, app))

    setup_dishka(container_factory(), app)


def init_routers(app: FastAPI) -> None:
    app.include_router(health_check_router)


def create_app() -> FastAPI:
    app = FastAPI()

    init_di(app)
    init_routers(app)
    init_exception_handlers(app)

    return app

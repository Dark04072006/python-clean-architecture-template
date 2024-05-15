from typing import cast

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.types import ExceptionHandler

from app.domain.common.exceptions import DomainValidationError


async def domain_validation_handler(
    request: Request,
    exc: DomainValidationError,
) -> JSONResponse:
    return JSONResponse(status_code=422, content={"message": exc.message})


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(
        DomainValidationError,
        cast(ExceptionHandler, domain_validation_handler),
    )

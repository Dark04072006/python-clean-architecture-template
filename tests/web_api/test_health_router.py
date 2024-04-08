from typing import Any, AsyncIterable, Awaitable, Callable, Coroutine, cast

import httpx
import pytest
import pytest_asyncio

from app.main.web_api import create_app

_Message = dict[str, Any]
_Receive = Callable[[], Awaitable[_Message]]
_Send = Callable[[dict[str, Any]], Coroutine[None, None, None]]
_ASGIApp = Callable[[dict[str, Any], _Receive, _Send], Coroutine[None, None, None]]


@pytest_asyncio.fixture
async def client() -> AsyncIterable[httpx.AsyncClient]:
    app = cast(_ASGIApp, create_app())
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(
        transport=transport, base_url="http://testserver"
    ) as client:
        yield client


@pytest.mark.asyncio
async def test_health_status_success_endpoint(client: httpx.AsyncClient) -> None:
    response = await client.get("/health-check/")

    assert response.status_code == 200
    assert response.json() == {"status": "Ok"}
    assert response.headers["Content-Type"] == "application/json"


@pytest.mark.asyncio
async def test_health_status_fail_endpoint(client: httpx.AsyncClient) -> None:
    response = await client.post("/health-check/")

    assert response.status_code == 405
    assert response.json() == {"detail": "Method Not Allowed"}
    assert response.headers["Content-Type"] == "application/json"

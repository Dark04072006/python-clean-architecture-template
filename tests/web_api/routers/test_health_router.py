import httpx
import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_health_status_success_endpoint(
    client: httpx.AsyncClient,
) -> None:
    response = await client.get("/health-check/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "Ok"}
    assert response.headers["Content-Type"] == "application/json"


@pytest.mark.asyncio
async def test_health_status_fail_endpoint(client: httpx.AsyncClient) -> None:
    response = await client.post("/health-check/")

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    assert response.json() == {"detail": "Method Not Allowed"}
    assert response.headers["Content-Type"] == "application/json"

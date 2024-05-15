from typing import Protocol, TypeVar

Request_contra = TypeVar("Request_contra", contravariant=True)
Response_co = TypeVar("Response_co", covariant=True)


class Interactor(Protocol[Request_contra, Response_co]):
    async def __call__(self, request: Request_contra) -> Response_co:
        raise NotImplementedError

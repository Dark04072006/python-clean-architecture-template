from dataclasses import dataclass
from typing import Generic, TypeVar

from app.domain.common.value_objects import ValueObject

EntityId = TypeVar("EntityId", bound=ValueObject)


@dataclass
class Entity(Generic[EntityId]):
    id: EntityId

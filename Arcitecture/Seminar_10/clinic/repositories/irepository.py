from typing import Any
from abc import ABC, abstractmethod


class IRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Any]:
        pass

    @abstractmethod
    def get_by_id(self, id: Any) -> Any:
        pass

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self, item: Any):
        pass

    @abstractmethod
    def delete(self, item: Any):
        pass

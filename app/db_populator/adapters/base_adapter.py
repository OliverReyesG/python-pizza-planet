from abc import ABC, abstractmethod
from typing import List


class BaseRepository(ABC):

    @abstractmethod
    def create(self, data: dict) -> tuple:
        raise NotImplementedError

    @abstractmethod
    def create_many(self, data: List[dict]) -> list:
        raise NotImplementedError

    @abstractmethod
    def list(self):
        raise NotImplementedError

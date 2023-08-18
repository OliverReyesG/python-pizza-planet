from abc import ABC, abstractmethod
from typing import List


class BaseRepository(ABC):

    def create_many(self, data: List[dict]) -> list:
        raise NotImplementedError

    def list(self):
        raise NotImplementedError

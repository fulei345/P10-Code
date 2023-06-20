from abc import ABC, abstractmethod
from typing import Any


class Logger(ABC):

    @abstractmethod
    def log(self, filename: str, out: str) -> None:
        pass

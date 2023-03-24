from abc import ABC, abstractmethod
from typing import Any


class Logger(ABC):

    @abstractmethod
    def log_crash(self, inp: Any, out: Any) -> None:
        pass

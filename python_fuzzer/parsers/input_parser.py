from typing import List, Any
from abc import ABC, abstractmethod


class InputParser(ABC):
    @abstractmethod
    def load_corpus(self) -> List[Any]:
        pass

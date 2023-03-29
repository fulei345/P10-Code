from abc import ABC, abstractmethod
from typing import Any, Tuple
from xml.etree.ElementTree import ElementTree


class Runner(ABC):
    @abstractmethod
    def run(self, document: ElementTree, filename: str) -> Tuple[Any, str]:
        pass

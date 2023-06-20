from abc import ABC, abstractmethod
from typing import Any, Tuple
from xml.etree.cElementTree import ElementTree


class Runner(ABC):
    @abstractmethod
    def run(self, document: ElementTree, filename: str) -> Tuple[str, str]:
        pass

from typing import List, Any
from abc import ABC, abstractmethod
from xml.etree.cElementTree import ElementTree

class InputParser(ABC):
    @abstractmethod
    def load_corpus(self) -> List[str]:
        pass

    @abstractmethod
    def parse_document(self, file) -> ElementTree:
        pass

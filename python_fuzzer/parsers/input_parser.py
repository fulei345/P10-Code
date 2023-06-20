from typing import List
from abc import ABC, abstractmethod
from xml.etree.cElementTree import ElementTree

class InputParser(ABC):
    @abstractmethod
    def load_corpus(self) -> List[ElementTree]:
        pass

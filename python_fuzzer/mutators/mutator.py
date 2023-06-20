from abc import ABC, abstractmethod
from xml.etree.cElementTree import ElementTree


class Mutator(ABC):
    @abstractmethod
    def mutate(self, inp: ElementTree) -> ElementTree:
        pass

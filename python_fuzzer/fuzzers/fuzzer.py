from abc import ABC, abstractmethod
from typing import List, Tuple
from xml.etree.cElementTree import ElementTree


class Fuzzer(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def fuzz(self) -> ElementTree:
        pass

    @abstractmethod
    def run(self) -> Tuple[str, str]:
        pass

    @abstractmethod
    def multiple_runs(self, run_count: int) -> List[Tuple[str, str]]:
        pass

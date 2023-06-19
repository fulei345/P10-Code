from typing import Set, Any
from xml.etree.cElementTree import ElementTree
import sys
sys.path.append("..")


class Seed:
    """Represent an input with additional attributes"""

    def __init__(self, data: ElementTree) -> None:
        """Initialize from seed data"""
        self.data: Any = data

        # These are needed for power schedules
        self.coverage: Set[str] = set()
        self.outcome: str = ""
        self.result: str = ""
        self.energy = 0.0
        self.chosen_count = 0
        self.population_name = "first"

    def __str__(self) -> str:
        """Returns data as string representation of the seed"""
        return self.data.__str__()

    __repr__ = __str__

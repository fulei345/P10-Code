from typing import List, Set, Union, Any
from xml.etree.cElementTree import Element, ElementTree, parse, ParseError


class Seed:
    """Represent an input with additional attributes"""

    # Type Should probably be ElementTree
    def __init__(self, data: Any) -> None:
        """Initialize from seed data"""
        self.data: Any = data

        # These will be needed for advanced power schedules
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
    
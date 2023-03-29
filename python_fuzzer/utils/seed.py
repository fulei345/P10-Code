from typing import List, Set, Union
from xml.etree.ElementTree import Element, ElementTree, parse, ParseError


class Seed:
    """Represent an input with additional attributes"""

    def __init__(self, data: ElementTree) -> None:
        """Initialize from seed data"""
        self.data: ElementTree = data

        # These will be needed for advanced power schedules
        self.coverage: Set[str] = set()
        # self.distance: Union[int, float] = -1
        self.energy = 0.0

    def __str__(self) -> str:
        """Returns data as string representation of the seed"""
        return self.data.__str__()

    __repr__ = __str__
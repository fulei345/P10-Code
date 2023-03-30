from typing import List, Set, Union, Any
from xml.etree.ElementTree import Element, ElementTree, parse, ParseError


class Seed:
    """Represent an input with additional attributes"""

    # Type Should probably be ElementTree
    def __init__(self, data: Any) -> None:
        """Initialize from seed data"""
        self.data: Any = data

        # These will be needed for advanced power schedules
        self.coverage: Set[str] = set()
        # self.distance: Union[int, float] = -1
        self.energy = 0.0

    def __str__(self) -> str:
        """Returns data as string representation of the seed"""
        return self.data.__str__()

    __repr__ = __str__
    
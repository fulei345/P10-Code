import random
from typing import Any, List, Callable
from xml.etree.cElementTree import ElementTree, tostring, fromstring, Element

from .mutator import Mutator
import sys

sys.path.append("..")
from utils import TypeGenerator

INTERESTING8 = [-128, -1, 0, 1, 16, 32, 64, 100, 127]
INTERESTING16 = [0, 128, 255, 256, 512, 1000, 1024, 4096, 32767, 65535]
INTERESTING32 = [0, 1, 32768, 65535, 65536, 100663045, 2147483647, 4294967295]


class FieldMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.replace_string_mutator,
                                                     self.replace_sub_mutator,
                                                     self.replace_char_mutator,
                                                     self.delete_sub_mutator,
                                                     self.delete_char_mutator,
                                                     self.add_sub_mutator,
                                                     self.add_char_mutator,
                                                     self.interesting8_mutator,
                                                     self.interesting16_mutator,
                                                     self.interesting32_mutator
                                                     ]
        # self.dont_mutate: List[str] = ["CustomizationID",
        #                                "CopyIndicator", "FreeOfChargeIndicator", "CatalogueIndicator", "HazardousRiskIndicator"
        #                                "IssueDate", "TaxPointDate", "ActualDeliveryDate", "LatestDeliveryDate", "Date", "TaxPointDate"]

    def mutate(self, document: ElementTree) -> ElementTree:
        """
        Mutate fields i OIOUBL document.
        :return: Mutated documents.
        """
        root: Element = document.getroot()
        total_size = sum(1 for _ in root.iter())
        mutator: Callable[[Any], Any] = random.choice(self.mutators)
        index: int = random.randint(1, total_size)
        for i, elem in enumerate(root.iter()):
            if i == index:
                if elem.text is None:
                    return document
                field: str = mutator(elem.text)
                elem.text = field
                return document
        return document

    # For now only string/char methods is implemented, can be changed to look for the current type
    def replace_string_mutator(self, data: str) -> str:
        c: str = TypeGenerator.make_string()
        return c

    def replace_sub_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        end_pos: int = random.randint(start_pos, len(data) - 1)
        c: str = TypeGenerator.make_string()

        data = data[:start_pos] + c + data[end_pos:]
        return data

    def replace_char_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        c: str = TypeGenerator.make_char()

        data = data[:start_pos] + c + data[start_pos + 1:]
        return data

    def delete_sub_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        end_pos: int = random.randint(start_pos, len(data) - 1)

        data = data[:start_pos] + data[end_pos:]
        return data

    def delete_char_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)

        data = data[:start_pos] + data[start_pos + 1:]
        return data

    def add_sub_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        c: str = TypeGenerator.make_string()

        data = data[:start_pos] + c + data[start_pos + 1:]
        return data

    def add_char_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        c: str = TypeGenerator.make_char()

        data = data[:start_pos] + c + data[start_pos + 1:]
        return data

    def interesting8_mutator(self, data: str) -> str:
        data = random.choice(INTERESTING8)
        return str(data)

    def interesting16_mutator(self, data: str) -> str:
        data = random.choice(INTERESTING16)
        return str(data)

    def interesting32_mutator(self, data: str) -> str:
        data = random.choice(INTERESTING32)
        return str(data)

import random
from typing import Any, List, Callable
from xml.etree.ElementTree import ElementTree, tostring, fromstring, Element
from dataclasses import dataclass, fields, field

from .mutator import Mutator
import sys

sys.path.append("..")
from invoice.invoice_structure import invoice_type_dict
from utils import TypeGenerator

INTERESTING8 = [-128, -1, 0, 1, 16, 32, 64, 100, 127]
INTERESTING16 = [0, 128, 255, 256, 512, 1000, 1024, 4096, 32767, 65535]
INTERESTING32 = [0, 1, 32768, 65535, 65536, 100663045, 2147483647, 4294967295]


class FieldMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.parent_map = dict()
        # List mutator functions here
        self.string_mutators: List[Callable[[Any], Any]] = [self.replace_string_mutator,
                                                     self.replace_sub_mutator,
                                                     self.replace_char_mutator,
                                                     self.delete_sub_mutator,
                                                     self.delete_char_mutator,
                                                     self.add_sub_mutator,
                                                     self.add_char_mutator
                                                     ]
        
        self.int_mutators: List[Callable[[Any], Any]] = [self.interesting8_mutator,
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
        index: int = random.randint(1, total_size)
        self.parent_map = {c:p for p in root.iter() for c in p}
        for i, elem in enumerate(root.iter()):            
            if i == index:
                parent_class_name = self.parent_map[elem].tag.split("}")[1]
                parent = invoice_type_dict[parent_class_name]
                field_type = str
                for f in fields(parent): 
                    if f.name == elem.tag.split("}")[1]:
                        field_type = f.type
                mutator: Callable[[Any], Any]
                if field_type == int:
                    mutator = random.choice(self.int_mutators)
                else:
                    mutator = random.choice(self.string_mutators)
                fiel: str = mutator(elem.text)
                elem.text = fiel
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

    # Should only be used when we know the type to be integer
    def addition_mutator(self, data: str) -> str:
        num_add: int = random.randint(1, 36)
        num = int(data)

        num = num + num_add
        return str(num)
    
    # Should only be used when we know the type to be integer
    def subtraction_mutator(self, data: str) -> str:
        num_sub: int = random.randint(1, 36)
        num = int(data)

        num = num + num_sub
        return str(num)

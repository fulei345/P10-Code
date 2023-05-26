import random
from typing import Any, List, Callable, get_origin, Union, get_args
from xml.etree.cElementTree import ElementTree, fromstring, Element
from dataclasses import fields
from datetime import date, time
from .mutator import Mutator
import sys

sys.path.append("..")
from invoice import invoice_type_dict
from utils import TypeGenerator
from config import NOT_PROB

INTERESTING8 = [-128., -1., 0., 1., 16., 32., 64., 100., 127.]
INTERESTING16 = [0., 128., 255., 256., 512., 1000., 1024., 4096., 32767., 65535.]
INTERESTING32 = [0., 1., 32768., 65535., 65536., 100663045., 2147483647., 4294967295.]


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
                field_type = None
                class_name = elem.tag.split("}")[1]
                for f in fields(parent):
                    if f.name == class_name:
                        #check if the field is optional (as its type is then Union(type, None)) or list and set field_type to its type
                        if get_origin(f.type) in [Union, list] :
                            field_type = get_args(f.type)[0]
                            #check if it is still list as optional comes before list if it has both
                            if get_origin(field_type) == list:
                                field_type = get_args(field_type)[0]
                        else:
                            field_type = f.type
                self.field_type = field_type
                # if it is under this do not take the type into account
                if random.random() < NOT_PROB:
                    mutator = random.choice(self.string_mutators)
                else:
                    mutator = self.generate_type_mutator
                if elem.text is None or elem.text == "":
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
    
    def generate_type_mutator(self, data: str) -> str:
        data: str
        if self.field_type == str:
            data = TypeGenerator.make_string()
        elif self.field_type == bool:
            data = TypeGenerator.make_bool()
        elif self.field_type == time:
            data = TypeGenerator.make_time()
        elif self.field_type == date:
            data = TypeGenerator.make_date()
        elif self.field_type == bytes:
            data = TypeGenerator.make_string()
        elif self.field_type == float:
            float_mut = random.choice([TypeGenerator.make_float, TypeGenerator.make_float_thousands])
            data = float_mut
        else:
            print("fuck")

        return data
import random
from typing import Any, List, Callable, get_origin, Union, get_args
from xml.etree.cElementTree import ElementTree, Element
from dataclasses import fields
from datetime import date, time
from .mutator import Mutator
import sys

sys.path.append("..")
from models import invoice_type_dict
from codelists import names_list, codelist_list
from utils import TypeGenerator
from config import TYPE_PROB


INTERESTING8 = [-128., -1., 0., 1., 16., 32., 64., 100., 127.]
INTERESTING16 = [0., 128., 255., 256., 512., 1000., 1024., 4096., 32767., 65535.]
INTERESTING32 = [0., 1., 32768., 65535., 65536., 100663045., 2147483647., 4294967295.]


class FieldMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.parent_map: dict = dict()
        # List mutator functions here
        self.string_mutators: List[Callable[[Any], Any]] = [self.replace_string_mutator,
                                                     self.replace_sub_mutator,
                                                     self.replace_char_mutator,
                                                     self.delete_sub_mutator,
                                                     self.delete_char_mutator,
                                                     self.add_sub_mutator,
                                                     self.add_char_mutator,
                                                     self.codelist_mutator
                                                     ]

        self.interesting_floats: List[Callable[[], Any]] = [self.interesting8_mutator,
                                                     self.interesting16_mutator,
                                                     self.interesting32_mutator
                                                     ]

    def mutate(self, document: ElementTree) -> ElementTree:
        """
        Mutate fields i OIOUBL document.
        :return: Mutated documents.
        """
        root: Element = document.getroot()
        # map all non root elements to their parent
        self.parent_map: dict = {c:p for p in root.iter() for c in p}
        # choose random element
        index: int = random.randint(1, len(self.parent_map) + 1)
       
        #loop through elements until index is reached
        for i, elem in enumerate(root.iter()):
            if i == index:
                # if the chosen field dont have text return
                if elem.text is None or elem.text == "":
                    return document
                
                #find name of parent class
                self.parent_class_name: str = self.parent_map[elem].tag.split("}")[1]

                # choose if type should not be taken into account
                if random.random() < TYPE_PROB:
                    self.field_name: str = elem.tag.split("}")[1]
                    mutator = random.choice(self.string_mutators)
                else:
                    # fiind the classtype of parent
                    parent = invoice_type_dict[self.parent_class_name]
                    field_type = None
                    # get name of the chosen element
                    class_name: str = elem.tag.split("}")[1]
                    # loop through parent elements fields until the chosen field is encountered
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

                    mutator = self.generate_type_mutator

                field: str = mutator(elem.text)
                elem.text = field
                return document
        return document

    # replace full string
    def replace_string_mutator(self, data: str) -> str:
        c: str = TypeGenerator.make_string()
        return c
    
    # replace substring
    def replace_sub_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        end_pos: int = random.randint(start_pos, len(data) - 1)
        c: str = TypeGenerator.make_string()

        data = data[:start_pos] + c + data[end_pos:]
        return data

    # replace char in the string
    def replace_char_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        c: str = TypeGenerator.make_char()

        data = data[:start_pos] + c + data[start_pos + 1:]
        return data

    # delete substring
    def delete_sub_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        end_pos: int = random.randint(start_pos, len(data) - 1)

        data = data[:start_pos] + data[end_pos:]
        return data
    
    # delete char from the string
    def delete_char_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)

        data = data[:start_pos] + data[start_pos + 1:]
        return data

    # add substring to the string
    def add_sub_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        c: str = TypeGenerator.make_string()

        data = data[:start_pos] + c + data[start_pos + 1:]
        return data

    # add char to the string
    def add_char_mutator(self, data: str) -> str:
        start_pos: int = random.randint(0, len(data) - 1)
        c: str = TypeGenerator.make_char()

        data = data[:start_pos] + c + data[start_pos + 1:]
        return data

    def interesting8_mutator(self) -> str:
        data = random.choice(INTERESTING8)
        return str(data)

    def interesting16_mutator(self) -> str:
        data = random.choice(INTERESTING16)
        return str(data)

    def interesting32_mutator(self) -> str:
        data = random.choice(INTERESTING32)
        return str(data)
    
    # generate text based on the type of the field
    def generate_type_mutator(self, data: str) -> str:
        new_data: str = ""
        if self.field_type == str:
            mutator = random.choice(self.string_mutators)
            new_data = mutator(data)
        elif self.field_type == bool:
            new_data = TypeGenerator.make_bool()
        elif self.field_type == time:
            new_data = TypeGenerator.make_time()
        elif self.field_type == date:
            new_data = TypeGenerator.make_date()
        elif self.field_type == bytes:
            new_data = TypeGenerator.make_string()
        elif self.field_type == float:
            # random choice of making new floats, new ints, new floats with thousands separation or interesting values
            float_mut = random.choice([TypeGenerator.make_float, TypeGenerator.make_float_thousands, TypeGenerator.make_int, self.interesting8_mutator, self .interesting16_mutator, self.interesting32_mutator])

            new_data = float_mut()

        return new_data
    
    # Sets a field to one from its codelist or just call another mutator
    def codelist_mutator(self, data: str) -> str:
                
        # Check if it has a codelist, if it does take one of those
        for i, name in enumerate(names_list):

            if "-" in name and self.parent_class_name not in name:
                continue            

            if self.field_name in name and ("Code" in self.field_name or "ID" in self.field_name):
                new_data = random.choice(codelist_list[i])
                return new_data
            
        mutator = random.choice(self.string_mutators[:-1])
        new_data: str = mutator(data)
        return new_data

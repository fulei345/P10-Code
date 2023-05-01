import random
from typing import Any, List, Callable, Optional
from xml.etree.ElementTree import ElementTree, Element, SubElement
from dataclasses import dataclass, fields
from datetime import date, time
import string

from .mutator import Mutator

import sys
sys.path.append("..")
from invoice import Invoice
from utils import TypeGenerator


class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.root = None
        self.parent_map = dict()
        self.total_size = 0
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.insert_field,
                                                     self.delete_field,
                                                     self.move_field,
                                                     self.add_field]

    def mutate(self, document: ElementTree) -> ElementTree:
        """
        Mutate the structure of fields in an OIOUBL document.
        :return: Mutated documents.
        """
        root:Element = document.getroot()
        self.total_size = sum(1 for _ in root.iter())
        # mapper alle elementer til deres parent element
        self.parent_map = {c:p for p in root.iter() for c in p}
        self.root = root
        mutator: Callable[[Any], Any] = random.choice(self.mutators)
        if mutator == self.add_field:
            mutator(root)
        else:
            index: int = random.randint(1, self.total_size)
            for i, elem in enumerate(root.iter()):
                if i == index:
                    mutator(self.parent_map[elem], elem)
                    return document
        return document

    # when used directly it insert duplicate of the field - is also used to insert fields when moving fields or add new fields
    def insert_field(self, parent: Element, subelement: Element) -> Element:
        # 50% sætte i parent eller uniformt i hele file
        if(random.random() < 0.5 ):
            index = random.randint(0, len(parent))
            parent.insert(index, subelement) #insert field in parent class
        else:
            index = random.randint(1, self.total_size)
            for i, elem in enumerate(self.root.iter()):
                if i == index:
                    parent = self.parent_map[elem]
                    insert_index = random.randint(0, len(parent))
                    parent.insert(insert_index, subelement)
                    return parent
        return parent


    def delete_field(self, parent: Element, subelement: Element) -> Element:
        
        parent.remove(subelement)
        
        return parent
    

    def move_field(self, parent: Element, subelement: Element) -> Element:
        
        parent.remove(subelement)
        
        self.insert_field(parent, subelement)
        
        return parent
        
    #create new field and insert in the document
    def add_field(self, parent: Element) -> Element:
        #TODO probably make this general so it could be other types of documents as well (if their structure was made lol)
        #randomly choose one of the Invoice direct subelements to create        
        field = random.choice(fields(Invoice))
        
        elem = self.make_element(field)

        self.insert_field(parent, elem)

        return parent
    
    def make_element(self, field) -> Element:
        
        #make element with the name
        elem = Element(field.name)

        #makes text for element according to its field type
        if field.type == str: #or field.type == Optional[str]:
            elem.text = TypeGenerator.make_string()
        elif field.type == int: #or field.type == Optional[int]:
            elem.text = TypeGenerator.make_int()
        elif field.type == bool: #or field.type == Optional[bool]:
            elem.text = TypeGenerator.make_bool()
        elif field.type == time: #or field.type == Optional[time]:
            elem.text = TypeGenerator.make_time()
        elif field.type == date: #or field.type == Optional[date]:
            elem.text = TypeGenerator.make_date()
        elif field.type == bytes: #or field.type == Optional[bytes]:
            elem.text = TypeGenerator.make_string() #TODO change this (look at oioubl documentation for attachement binary object)
        elif field.type == float: #or field.type == Optional[float]:
            elem.text = TypeGenerator.make_float()
        else:
            elem = self.make_subclass(elem, field.type)
            
        return elem   
    
    def make_subclass(self, elem: Element, type) -> Element:   

        # finds the fields of the dataclass type          
        names = fields(type) 
        
        # make elements for all the class fields iteratively
        for field in names:
            subelem = self.make_element(field)
            elem.append(subelem)
                
        return elem

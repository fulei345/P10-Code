import random
from typing import Any, List, Callable, Optional, get_origin, Union, get_args
from xml.etree.cElementTree import ElementTree, Element
from dataclasses import dataclass, fields
from datetime import date, time
import string

from .mutator import Mutator

import sys
sys.path.append("..")
from invoice import Invoice
from utils import TypeGenerator
from config import DUPLICATE_PROB, OPT_PROP


class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.root = None
        self.parent_map = dict()
        self.total_size = 0
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.duplicate_field,
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
    
    def check_if_ancestor(self, ancestor: Element, subelement: Element) -> bool:
        parent = self.parent_map[ancestor]
        child = parent
        while subelement != parent:
            if parent not in self.parent_map or child not in self.parent_map:
                return True
            else:
                temp_p = parent
                parent = self.parent_map[child]
                child = temp_p
        return False

    def duplicate_field(self, parent: Element, subelement: Element) -> Element:
        if(random.random() < DUPLICATE_PROB ):
            #find the fields index in the parent element and duplicate it there
            index = list(parent).index(subelement)
            parent.insert(index, subelement) #insert field in parent class
        else:
            self.insert_field(parent, subelement)
        return parent

    # insert field at random place
    def insert_field(self, parent: Element, subelement: Element) -> Element:
        index = random.randint(1, self.total_size)
        for i, elem in enumerate(self.root.iter()):
            if i >= index and self.check_if_ancestor(elem, subelement): 
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
        elem = Element("{" + "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" + "}" + field.name)

        field_type = None
        
        #check if the field is optional (as its type is then Union(type, None)) and set field_type to its type
        if(get_origin(field.type) is Union):
            field_type = get_args(field.type)[0]
        else:
            field_type = field.type
        
        #makes text for element according to its field type
        if field_type == str: 
            elem.text = TypeGenerator.make_string()
        elif field_type == int: 
            elem.text = TypeGenerator.make_int()
        elif field_type == bool: 
            elem.text = TypeGenerator.make_bool()
        elif field_type == time: 
            elem.text = TypeGenerator.make_time()
        elif field_type == date: 
            elem.text = TypeGenerator.make_date()
        elif field_type == bytes: 
            elem.text = TypeGenerator.make_string() #TODO change this (look at oioubl documentation for attachement binary object)
        elif field_type == float: 
            elem.text = TypeGenerator.make_float()
        else:
            #change namespace to class namespace
            elem = Element("{" + "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" + "}" + field.name)
            elem = self.make_subclass(elem, field_type)
            
        return elem   
    
    def make_subclass(self, elem: Element, type) -> Element:   

        # finds the fields of the dataclass type          
        names = fields(type) 
               
        # make elements for all the class fields iteratively
        for field in names:
            if(not get_origin(field.type) is Union or random.random() < OPT_PROP):   
                subelem = self.make_element(field)
                elem.append(subelem)
                
        return elem

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



class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.root = None
        self.parent_map = dict()
        self.total_size = 0
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.add_field]

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
        index: int = random.randint(0, self.total_size)
        counter: int = 0
        for elem in root.iter():
            if counter == index:
                mutator: Callable[[Any], Any] = random.choice(self.mutators)
                mutator(self.parent_map[elem], elem)
                #for elem in root.iter():
                #    print(elem)
                #    if elem.tag == 'test':
                #        print(elem.text)
                return document
            counter += 1
        return document

    # when used directly it insert duplicate of the field - is also used to insert fields when moving fields or add new fields
    def insert_field(self, parent: Element, subelement: Element) -> Element:
        # 50% sætte i parent eller uniformt i hele file
        if(random.random() < 0.5 ):
            index = random.randint(0, len(parent))
            parent.insert(index, subelement) #insert field in parent class
        else:
            index = random.randint(0, self.total_size)
            counter = 0
            for elem in self.root.iter():
                if counter == index:
                    parent = self.parent_map[elem]
                    insert_index = random.randint(0, len(parent))
                    parent.insert(insert_index, subelement)
                counter += 1

        return parent


    def delete_field(self, parent: Element, subelement: Element) -> Element:
        
        parent.remove(subelement)
        
        return parent
    

    def move_field(self, parent: Element, subelement: Element) -> Element:
        
        parent.remove(subelement)
        
        self.insert_field(parent, subelement)
        
        return parent
        
    #create new field and insert in the document
    def add_field(self, parent: Element, subelement: Element) -> Element:
        
        #f = fields(Invoice)
        
        field = random.choice(fields(Invoice))
        
        print(field)
        
        elem = self.make_element(field)

            
        #for field in f:
        #    print(field.name, field.type)
        #    if field.type == date or field.type == Optional[date]:
        #        print("\nyo\n")

        # chose one randomly
            # just from toplevel (invoice)? 
                # list with direct subelements for invoice (+their types?)
            # or from all? 
                # then all subclasses also needs lists :(
        # if field is just an element
            # build element (make a random variable with the according type, make element with the variable as its text value)
        # if it is a subclass 
            # build class (build all its subelements iteratively)

        #xml.etree.ElementTree.SubElement(parent, tag, attrib={}, **extra)
            #Subelement factory. This function creates an element instance, and appends it to an existing element.

        #a = SubElement(parent, 'test')
        #a.text = 'bob'
        
        print(elem.text)
        
        for sub in elem.iter():
            print(sub)

        self.insert_field(parent, elem)

        return parent
    
    def make_element(self, field) -> Element:
        
        elem = Element(field.name)

        if field.type == str: #or field.type == Optional[str]:
            elem.text = self.make_string()
            print("\n1\n")
        elif field.type == int: #or field.type == Optional[int]:
            elem.text = self.make_int()
            print("\n2\n")
        elif field.type == bool: #or field.type == Optional[bool]:
            elem.text = self.make_bool()
            print("\n3\n")
        elif field.type == time: #or field.type == Optional[time]:
            elem.text = self.make_time()
            print("\n4\n")
        elif field.type == date: #or field.type == Optional[date]:
            elem.text = self.make_date()
            print("\n5\n")
        elif field.type == bytes: #or field.type == Optional[date]:
            elem.text = self.make_string() #TODO change this (look at oioubl documentation for attachement binary object)
            print("\n7\n")
        else:
            print("\n6\n")
            elem = self.make_subclass(elem, field.type)
            
        return elem   
    
    def make_subclass(self, elem: Element, type) -> Element:   
           
        names = fields(type) 
        
        for field in names:
            subelem = self.make_element(field)
            elem.append(subelem)
        
        print(elem)
        
        return elem
            
        
    def make_string(self) -> str:

        length = random.randint(0, 100)     

        text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
        
        return text
    
    def make_int(self) -> str:
        text = random.randint(0, sys.maxsize)
        
        return str(text)
        
    def make_bool(self) -> str:
        if(random.random() < 0.5 ):
            text = "false"
        else:
            text = "true"
        
        return text
            
    def make_time(self) -> str:
        #creat time with random values, first argument is hours, second argument is minutes, and last argument is seconds 
        text = time(random.randint(0, 23), random.randint(0, 60), random.randint(0, 60)) 
        
        return str(text)
            
    def make_date(self) -> str:
        #creat date with random values, first argument is year with the range for datetime modules minyear and maxyear, second argument is month, and last argument is day 
        text = date(random.randint(1, 9999), random.randint(1, 12), random.randint(1, 31)) 
        
        return str(text)
    
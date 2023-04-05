import random
from typing import Any, List, Callable
from xml.etree.ElementTree import ElementTree, Element

from .mutator import Mutator

class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.root = None
        self.parent_map = dict()
        self.total_size = 0
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.add_field,
                                                     self.delete_field,
                                                     self.move_field]

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
                return document
            counter += 1
        return document

    def add_field(self, parent: Element, subelement: Element) -> Element:
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
        
        self.add_field(parent, subelement)
        
        return parent
        
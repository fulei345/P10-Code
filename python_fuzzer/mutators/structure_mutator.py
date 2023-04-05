import random
from typing import Any, List, Callable
from xml.etree.ElementTree import ElementTree, Element

from .mutator import Mutator

class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.root = None
        self.parent_map = dict()
        self.root_size = 0
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
        self.root_size = sum(1 for _ in root.iter())
        self.parent_map = {c:p for p in root.iter() for c in p}
        self.root = root
        i: int = random.randint(0, self.root_size)
        j: int = 0
        for elem in root.iter():
            if j == i:
                mutator: Callable[[Any], Any] = random.choice(self.mutators)
                mutator(self.parent_map[elem], elem)
                return document
            j += 1
        return document

    def add_field(self, parent: Element, subelement: Element) -> Element:
        lollllllll = random.randint(0, 1)    

        if(lollllllll):
            index = random.randint(0, len(parent))
            parent.insert(index, subelement) #insert field in parent class
        else:
            index = random.randint(0, self.root_size)
            l = 0
            for elem in self.root.iter():
                if l == index:
                    parent = self.parent_map[elem]
                    k = random.randint(0, len(parent))
                    parent.insert(k, subelement)
                l += 1

        return parent


    def delete_field(self, parent: Element, subelement: Element) -> Element:
        
        parent.remove(subelement)
        
        return parent
    

    def move_field(self, parent: Element, subelement: Element) -> Element:
        
        parent.remove(subelement)
        
        self.add_field(parent, subelement)
        
        return parent
import random
from typing import Any, List, Callable
from xml.etree.ElementTree import ElementTree, Element

from .mutator import Mutator

class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.duplicate_field,
                                                     self.delete_field,
                                                     self.move_field]

    def mutate(self, document: ElementTree) -> ElementTree:
        """
        Mutate the structure of fields in an OIOUBL document.
        :return: Mutated documents.
        """
        #if(elem): # checks if the element has children, is true if it has
        root:Element = document.getroot()
        count = sum(1 for _ in root.iter())
        parent_map = {c:p for p in root.iter() for c in p}
        i: int = random.randint(0, count)
        j: int = 0
        parent = root
        print(i)
        for elem in root.iter():
            #if(elem): # checks if the element has children, is true if it has
            #    parent = elem
            if j == i:
                mutator: Callable[[Any], Any] = random.choice(self.mutators)
                print(elem)
        
                print(parent_map[elem], "\n")
                mutator(parent_map[elem], elem)
                print("\ngambling\n")
                for elem in root.iter():
                    print(elem)
                return document
            j += 1
        return document

    def duplicate_field(self, element: Element, subelement: Element) -> Element:
        index = 5 #random 
        print("yo")
        element.insert(index, subelement) #insert field in parent class(or the other)
        for elem in element.iter():
            print(elem)

        return element


    def delete_field(self, element: Element, subelement: Element) -> ElementTree:
        
        element.remove(subelement)
        
        for elem in element.iter():
            print(elem)  
        
        return element
    

    def move_field(self, element: Element, subelement: Element) -> ElementTree:
                
        print(element)
        print(len(element))
        print(subelement)
        print(len(subelement))
        
        element.remove(subelement)
        
        index = 5 #random 
        
        element.insert(index, subelement) #insert field in parent class(or the other)
        
        #for elem in element.iter():
        #    print(elem)  
        
        return element
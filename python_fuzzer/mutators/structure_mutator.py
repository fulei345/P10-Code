import random
from typing import Any, List, Callable, get_origin, Union, get_args, ForwardRef
from xml.etree.cElementTree import ElementTree, Element
from dataclasses import fields, Field
from datetime import date, time

from .mutator import Mutator

import sys
sys.path.append("..")
from models import Invoice, invoice_type_dict, Party, InvoiceLine, GoodsItem, Package, PriceList, attributes
from codelists import names_list, codelist_list, attributes_list
from utils import TypeGenerator
from config import PLACEMENT_PROB, OPT_PROB, MAX_RECUR_DEPTH


class StructureMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        self.root = None
        self.parent_map = dict()
        self.total_size = 0
        self.recur_level = 0
        # List of mutator functions
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
        # mapper alle elementer til deres parent element
        self.parent_map = {c:p for p in root.iter() for c in p}
        self.total_size = len(self.parent_map) + 1
        self.root = root
        self.recur_level = 0
        #choose random mutator
        mutator: Callable[[Any], Any] = random.choice(self.mutators)
        # if the mutator is add field, call directly
        if mutator == self.add_field:
            mutator(root)
        #else choose random index for an element for the mutation, find the element at index and call mutator
        else:
            index: int = random.randint(1, self.total_size)
            for i, elem in enumerate(root.iter()):
                if i == index:
                    mutator(self.parent_map[elem], elem)
                    return document
        return document

    # check if an element is not an ancestor of another element
    def check_if_not_ancestor(self, element: Element, element_to_check: Element) -> bool:
        parent = self.parent_map[element]
        # child is initialized to parent such that it can be used to find the parent of the parent in the first iteration
        child = parent
        # if element_to_check is equal to parent it is an ancestor
        while element_to_check != parent:
            #if the parent is not in parent map, it is the root element and not an ancestor
            if parent not in self.parent_map:
                return True
            #else find the parent of the parent and set child to current parent
            else:
                temp_p = parent
                parent = self.parent_map[child]
                child = temp_p
        return False
    

    def duplicate_field(self, parent: Element, subelement: Element) -> Element:
        if(random.random() < PLACEMENT_PROB):
            #find the fields index in the parent element and duplicate it there
            index: int = list(parent).index(subelement)
            parent.insert(index, subelement) #insert field in parent class
        else:
            #insert at random place
            self.insert_field(parent, subelement)
        return parent

    # insert field at random place
    def insert_field(self, parent: Element, subelement: Element) -> Element:
        index: int = random.randint(1, self.total_size)
        for i, elem in enumerate(self.root.iter()):
            # check that the subelement is not an ancestor of the element it is inserted into, as it would then be inserted in itself
            if i >= index and self.check_if_not_ancestor(elem, subelement):
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
        #TODO make this general so it could be other types of documents as well
        #randomly choose one of the Invoice direct subelements to create

        #set parent name
        self.parent_class_name = parent.tag.split("}")[1]

        #insert at correct index
        if random.random() < PLACEMENT_PROB:
            #choose random index
            index: int = random.randint(0, len(fields(Invoice)) - 1)
            #find field at the index
            field: Field = fields(Invoice)[index]
            counter: int = 0
            
            # loop through elements in parent class
            for i, elem in enumerate(parent):
                # find name of elem
                elem_name = elem.tag.split("}")[1]
                #if elem is the chosen field, make element and insert in parent at index 
                if elem_name == field.name:
                    subelement = self.make_element(field)
                    parent.insert(i, subelement)
                    return parent
                # loop through possible fields in an invoice document, starting from a counter for the latest elements position, until field matching the element is encountered
                while elem_name != fields(Invoice)[counter].name:
                    #increment counter
                    counter += 1
                    #if the counter is above the index, the position to insert element is found and the element is made and inserted in parent at index of outer loop
                    if counter > index:
                        subelement = self.make_element(field)
                        parent.insert(i, subelement)
                        return parent
        #insert random place in document
        else:
            field: Field = random.choice(fields(Invoice))
            elem: Element = self.make_element(field)
            self.insert_field(parent, elem)

        #below code is for making invoice document from the ground (change with the rest)
        #root = Element("<Invoice xmlns=\"urn:oasis:names:specification:ubl:schema:xsd:Invoice-2\" xmlns:cac=\"urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2\" xmlns:cbc=\"urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2\" xmlns:ccts=\"urn:oasis:names:specification:ubl:schema:xsd:CoreComponentParameters-2\" xmlns:sdt=\"urn:oasis:names:specification:ubl:schema:xsd:SpecializedDatatypes-2\" xmlns:udt=\"urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"urn:oasis:names:specification:ubl:schema:xsd:Invoice-2 UBL-Invoice-2.0.xsd\">")
        #elem = self.make_class(root, Invoice)
        #parent = elem
        return parent

    #make new element
    def make_element(self, field: Field) -> Element:

        self.recur_level += 1

        #make element with the field name
        elem: Element = Element("{" + "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2" + "}" + field.name)

        # Check if that field has a codelist and make it
        for i, name in enumerate(names_list):
            
            if "-" in name and self.parent_class_name not in name:
                continue

            if field.name in name and ("Code" in field.name or "ID" in field.name):
                elem.text = random.choice(codelist_list[i])
                self.recur_level -= 1
                return elem
            

        field_type = None

        #check if the field is optional (as its type is then Union(type, None)) or list and set field_type to its type
        if(get_origin(field.type) in [Union, list]):
            field_type = get_args(field.type)[0]
            #check if it it still list as optional comes before list if it has both
            if get_origin(field_type) == list:
                field_type = get_args(field_type)[0]
        else:
            field_type = field.type

        #makes text for element according to its field type
        if field_type == str:
            elem.text = TypeGenerator.make_string()
            if field.name.endswith("Code"):
                for attrib in attributes[0]:
                    val: str = TypeGenerator.make_string()
                    elem.set(attrib, val)
            elif field.name.endswith("ID"):
                for attrib in attributes[1]:
                    val: str = TypeGenerator.make_string()
                    elem.set(attrib, val)
            elif not field.name.endswith("Percent"):
                for attrib in attributes[2]:
                    val: str = TypeGenerator.make_string()
                    elem.set(attrib, val)
        elif field_type == bool:
            elem.text = TypeGenerator.make_bool()
        elif field_type == time:
            elem.text = TypeGenerator.make_time()
        elif field_type == date:
            elem.text = TypeGenerator.make_date()
        elif field_type == bytes:
            elem.text = TypeGenerator.make_string()
            for attrib in attributes[5]:
                val: str = TypeGenerator.make_string()
                elem.set(attrib, val)
        elif field_type == float:
            float_mut = random.choice([TypeGenerator.make_float, TypeGenerator.make_float_thousands])
            elem.text = float_mut()
            if field.name.endswith(("Quantity", "Measure")):
                for attrib in attributes[3]:
                    val: str = TypeGenerator.make_string()
                    elem.set(attrib, val)
            elif field.name.endswith("Amount"):
                for attrib in attributes[4]:
                    val: str = TypeGenerator.make_string()
                    elem.set(attrib, val)
        else:
            #set parent name
            self.parent_class_name = field.name

            #change namespace to class namespace
            elem = Element("{" + "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2" + "}" + field.name)
            elem = self.make_class(elem, field_type)

        self.recur_level -= 1
        return elem

    # make new class element
    def make_class(self, elem: Element, type) -> Element:

        self.recur_level += 1


        #if above max recursion level return without making elements of the class
        if(self.recur_level > MAX_RECUR_DEPTH):
            self.recur_level -= 1
            return elem

        #if the type is a forward reference change it to the actual type
        if(isinstance(type, ForwardRef)):
            type = type._evaluate(locals(), globals(), frozenset())

        # finds the fields of the dataclass type
        names = fields(type)

        field_type = None

        # make elements for all the class fields iteratively
        for field in names:
            #check if the field is optional (as its type is then Union(type, None)) and change type to actual type or skip at a specified probability
            if get_origin(field.type) is Union:
                if random.random() < OPT_PROB:
                    field_type = get_args(field.type)[0]
                else:
                    continue
            else:
                #set type
                field_type = field.type
            #check if type is list
            if get_origin(field_type) == list:
                #find actual type 
                field_type = get_args(field_type)[0]
                i: int = 0
                # chose random amount, between 1 and 5, of the element to be made 
                amount: int = random.randint(1,5)
                while i < amount:
                    subelem: Element = self.make_element(field)
                    elem.append(subelem)
                    i += 1
            #else just make element
            else:
                    subelem: Element = self.make_element(field)
                    elem.append(subelem)

        self.recur_level -= 1
        return elem

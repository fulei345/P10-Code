import random
from typing import Any, List, Callable
from xml.etree.ElementTree import ElementTree, tostring, fromstring, Element

from .mutator import Mutator


class DocumentMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        # List mutator functions here
        self.mutators: List[Callable[[Any], Any]] = [self.flip_bit_mutator,
                                                     self.add_to_byte_mutator]

    def mutate(self, document: ElementTree) -> ElementTree:
        """
        Mutate fields i OIOUBL document ??.
        :return: Mutated documents.
        """
        root:Element = document.getroot()
        for elem in root.iter():
            mutator: Callable[[Any], Any] = random.choice(self.mutators)
            text = elem.text
            # random variable to determine whether the element should be mutated - 15% probability currently
            i: int = random.randint(0, 99)
            if "\n" not in text and i > 84: 
                field: bytes = bytes(elem.text, 'utf-8')
                field = mutator(field)
                temp = str(field)
                elem.text = temp[2:-1]
        return document

    #string methods of this
    def flip_bit_mutator(self, data: bytes) -> bytes:
        pos: int = random.randint(0, len(data) - 1)
        bit: int = 1 << random.randint(0, 6)
        c: int = data[pos] ^ bit

        data = data[:pos] + bytes([c]) + data[pos + 1:]

        return data

    def add_to_byte_mutator(self, data: bytes) -> bytes:
        pos: int = random.randint(0, len(data) - 1)
        c = data[pos] + random.randint(1, 36)

        data = data[:pos] + bytes([c]) + data[pos + 1:]

        return data

    def remove_from_byte_mutator(self, data: bytes) -> bytes:
        pos: int = random.randint(0, len(data) - 1)
        c = data[pos] - random.randint(1, 36)

        data = data[:pos] + bytes([c]) + data[pos + 1:]

        return data

import random
from typing import Any, List, Callable
from xml.etree.cElementTree import ElementTree, tostring, fromstring, Element

if __name__ == "__main__":
    from mutator import Mutator
else:
    from .mutator import Mutator

import sys
sys.path.append("..")
from mutators import FieldMutator
from mutators import StructureMutator


class GeneralMutator(Mutator):
    def __init__(self, verbose: bool) -> None:
        self.verbose: bool = verbose
        # List mutator classes here
        self.mutator_classes: List[Mutator] = [StructureMutator(verbose)]

    def mutate(self, document: ElementTree) -> ElementTree:
        """
        Call another mutators mutate
        :return: Mutated documents.
        """
        # Randomly chooses a mutator class, could be set to one of them
        mutator = random.choice(self.mutator_classes)
        document, class_level = mutator.mutate(document)
        return document, class_level

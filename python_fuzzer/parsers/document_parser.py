import os
from typing import List, Any
from xml.etree.ElementTree import ElementTree, parse, ParseError

if __name__ == "__main__":
    from input_parser import InputParser
else:
    from .input_parser import InputParser


class DocumentParser(InputParser):
    def __init__(self, path: str, verbose: bool) -> None:
        self.path: str = path
        self.verbose: bool = verbose

    def load_corpus(self) -> List[ElementTree]:
        """
        Load OIOUBL documents from the fuzzer or example documents into a XML tree structure.
        :return: The corpus, which is the input to the fuzzer.
        """
        corpus = []

        # Find all files in folder
        files: List[str] = [file for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]
        # Filter for XML files
        files: List[str] = [file for file in files if file.endswith(".xml")]

        for file in files:
            path: str = os.path.join(self.path, file)
            if self.verbose:
                print(f"Parsing xml file: {file}")
            try:
                tree: ElementTree = parse(path)
                corpus.append(tree)
            except ParseError as err:
                print(f"Error Parsing the OIOUBL document: {err}")
        return corpus


if __name__ == "__main__":
    # Just for testing this class

    pass

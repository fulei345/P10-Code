import os
from typing import List, Any


if __name__ == "__main__":
    from input_parser import InputParser
else:
    from .input_parser import InputParser


class PacketParser(InputParser):
    def __init__(self, path: str, verbose: bool) -> None:
        self.path: str = path
        self.verbose: bool = verbose

    def load_seed(self) -> List[Any]:
        """
        TODO write this.
        """
        seed = []

        # Find all files in folder
        files = [file for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]
        return seed


if __name__ == "__main__":
    path: str = os.getcwd()
    path = os.path.dirname(path)
    path = os.path.join(path, "documents")

    parser: PacketParser = PacketParser(path)
    # The seed is a list of packet lists, which can contain packet lists themselves
    seed = parser.load_seed()
    # Here we access the first packet list of the seed
    packet = seed[0]

    print(packet.src, packet.dport, packet.sport)

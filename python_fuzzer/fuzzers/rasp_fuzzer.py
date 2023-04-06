import random
from typing import Any, List, Tuple
from xml.etree.ElementTree import ElementTree
from os.path import join

if __name__ == "__main__":
    from fuzzer import Fuzzer
else:
    from .fuzzer import Fuzzer

import sys
sys.path.append("..")
from mutators import DocumentMutator
from runners import RaspRunner
from loggers import FeedbackLogger
from parsers import DocumentParser


class RaspFuzzer(Fuzzer):
    def __init__(self,
                 corpus: List[str],
                 runner: RaspRunner,
                 mutator: DocumentMutator,
                 logger: FeedbackLogger,
                 verbose: bool,
                 parser: DocumentParser,
                 path: str,
                 mutation_count: int) -> None:

        self.corpus: List[str] = corpus
        self.corpus_size: int = len(self.corpus)
        self.seed_index: int = 0
        self.population: List[str] = []
        self.path: str = path
        self.verbose: bool = verbose

        self.runner: RaspRunner = runner
        self.logger: FeedbackLogger = logger
        self.mutator: DocumentMutator = mutator
        self.parser: DocumentParser = parser
        self.mutation_count: int = mutation_count

    def reset(self) -> None:
        self.population: List[str] = []
        self.seed_index = 0

    def fuzz(self, document: ElementTree) -> ElementTree:
        random_range = random.randint(1, self.mutation_count)
        for _ in range(random_range):
            document = self.mutator.mutate(document)
        return document

    def choose_candidate(self) -> str:

        if len(self.corpus) > 0 and self.seed_index < len(self.corpus):
            candidate: str = self.corpus[self.seed_index]
            self.seed_index += 1
            self.population.append(candidate)
            return candidate
        else:
            index: int = random.randint(0, len(self.population)-1)
            candidate: str = self.population[index]
            return candidate

    # TODO: Update when mutator is done
    def run(self) -> Tuple[Any, str]:
        path: str = self.choose_candidate()
        document: ElementTree = self.parser.parse_document(path)
        document: ElementTree  = self.fuzz(document)
        # Make new name
        filename: str = "fuzzed_document_" + str(self.seed_index) + ".xml"
        result, outcome, code_coverage = self.runner.run(document, filename)
        # Do something depending on the code coverage
        if outcome == "FAIL":
            document_path = join(self.path, filename)
            document.write(document_path, encoding="utf-8", xml_declaration=True)
            self.seed_index += 1
            self.population.append(path)
        return result, outcome

    def multiple_runs(self, run_count: int) -> List[Tuple[Any, str]]:
        results = [self.run() for _ in range(run_count)]
        # Filter results marked as "PASS"
        # TODO Better filter? Perhaps look at response from runner
        return [result for result in results if result[1] != "PASS"]

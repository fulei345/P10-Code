import random
from typing import Any, List, Tuple
from xml.etree.ElementTree import ElementTree

if __name__ == "__main__":
    from fuzzer import Fuzzer
else:
    from .fuzzer import Fuzzer

import sys
sys.path.append("..")
from mutators import DocumentMutator
from runners import RaspRunner
from loggers import SimpleLogger


class RaspFuzzer(Fuzzer):
    def __init__(self,
                 corpus: ElementTree,
                 runner: RaspRunner,
                 mutator: DocumentMutator,
                 logger: SimpleLogger,
                 verbose: bool,
                 mutation_count: int) -> None:

        self.corpus: ElementTree = corpus
        self.corpus_size: int = len(self.corpus)
        self.seed_index: int = 0
        self.population: List[ElementTree] = []

        self.verbose: bool = verbose

        self.runner: RaspRunner = runner
        self.logger: SimpleLogger = logger
        self.mutator: DocumentMutator = mutator
        self.mutation_count: int = mutation_count

    def reset(self) -> None:
        self.population = []
        self.seed_index = 0

    def fuzz(self, document: ElementTree) -> ElementTree:
        random_range = random.randint(1, self.mutation_count)
        for _ in range(random_range):
            document = self.mutator.mutate(document)
        return document

    def choose_candidate(self) -> Any:

        if len(self.corpus) > 0 and self.seed_index < len(self.corpus):
            candidate: ElementTree = self.corpus[self.seed_index]
            self.seed_index += 1
            self.population.append(candidate)
            return candidate
        else:
            index: int = random.randint(0, len(self.population)-1)
            candidate: ElementTree = self.population[index]
            return candidate

    # TODO: Update when mutator is done
    def run(self) -> Tuple[Any, str]:
        document: ElementTree = self.choose_candidate()
        document = self.fuzz(document)
        result, outcome = self.runner.run(document)
        if outcome == "FAIL":
            self.population.append(document)
        return result, outcome

    def multiple_runs(self, run_count: int) -> List[Tuple[Any, str]]:
        results = [self.run() for _ in range(run_count)]
        # Filter results marked as "PASS"
        # TODO Better filter? Perhaps look at respones from runner
        return [result for result in results if result[1] != "PASS"]


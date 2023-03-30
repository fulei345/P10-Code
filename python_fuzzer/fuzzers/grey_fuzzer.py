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
from utils import Seed
from scheduler import PowerSchedule

class GreyboxFuzzer(Fuzzer):
    def __init__(self,
                 seeds: list[ElementTree],
                 runner: RaspRunner,
                 mutator: DocumentMutator,
                 logger: FeedbackLogger,
                 schedule: PowerSchedule,
                 verbose: bool,
                 population_path: str,
                 mutation_count: int) -> None:

        self.seeds: list[ElementTree] = seeds

        self.seed_index: int = 0
        self.population: List[ElementTree] = []
        self.inputs: List[ElementTree] = []
        self.population_path: str = population_path
        self.verbose: bool = verbose

        self.schedule: PowerSchedule = schedule
        self.runner: RaspRunner = runner
        self.logger: FeedbackLogger = logger
        self.mutator: DocumentMutator = mutator
        self.mutation_count: int = mutation_count

        self.reset()

    def reset(self) -> None:
        """"Reset the initial population, seed index, coverage information"""
        self.coverages_seen = set()
        self.population = list(map(lambda x: Seed(x), self.seeds))
        self.seed_index: int = 0

    def create_candidate(self) -> str:
        """Returns an input generated by fuzzing a seed in the population"""
        seed = self.schedule.choose(self.population)

        # Stacking: Apply multiple mutations to generate the candidate
        candidate = seed.data
        num_mutations = random.randint(1, self.mutation_count)
        for _ in range(num_mutations):
            candidate = self.mutator.mutate(candidate)
        return candidate

    def fuzz(self, inp: Any) -> ElementTree:
        """Returns first each seed once and then generates new inputs"""
        if self.seed_index < len(self.seeds):
            # Still seeding
            self.inp = self.seeds[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()

        self.inputs.append(self.inp)
        return self.inp

    # TODO: Update when mutator is done
    def run(self) -> Tuple[Any, str]:
        document: ElementTree = self.fuzz("")
        # Make new name
        filename: str = "fuzzed_document_" + str(self.seed_index) + ".xml"
        result, outcome, _ = self.runner.run(document, filename)
        new_coverage = frozenset(self.runner.code_coverage)
        if new_coverage not in self.coverages_seen:
            # We have new coverage
            seed = Seed(self.inp)
            seed.coverage = self.runner.code_coverage
            self.coverages_seen.add(new_coverage)
            self.population.append(seed)
        return result, outcome

    def multiple_runs(self, run_count: int) -> List[Tuple[Any, str]]:
        results = [self.run() for _ in range(run_count)]
        # Filter results marked as "PASS"
        # Write all in population
        index = 0
        for seed in self.population:
            filename: str = "fuzzed_document_" + str(index) + ".xml"
            index += 1
            document_path = join(self.population_path, filename)
            seed.data.write(document_path, encoding="utf-8", xml_declaration=True)
        for cov in self.coverages_seen:
            print(cov)
        # TODO Better filter? Perhaps look at response from runner
        return [result for result in results if result[1] != "PASS"]
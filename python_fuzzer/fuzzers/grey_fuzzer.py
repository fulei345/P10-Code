import random
from typing import Any, List, Tuple
from xml.etree.cElementTree import ElementTree
from os.path import join
from copy import deepcopy

from python_fuzzer import Mutator

if __name__ == "__main__":
    from fuzzer import Fuzzer
else:
    from .fuzzer import Fuzzer

import sys
sys.path.append("..")
from mutators import Mutator
from runners import RaspRunner
from loggers import FeedbackLogger
from utils import Seed
from scheduler import PowerSchedule
from config import MUTATION_COUNT

class GreyboxFuzzer(Fuzzer):
    def __init__(self,
                 seeds: List[ElementTree],
                 runner: RaspRunner,
                 mutator: Mutator,
                 logger: FeedbackLogger,
                 schedule: PowerSchedule,
                 verbose: bool,
                 population_path: str,
                 mutation_count: int) -> None:

        self.seeds: List[ElementTree] = seeds

        self.seed_index: int = 0
        self.population: List[Seed] = []
        self.population_path: str = population_path
        self.verbose: bool = verbose
        self.total_coverage = set()

        self.schedule: PowerSchedule = schedule
        self.runner: RaspRunner = runner
        self.logger: FeedbackLogger = logger
        self.mutator: Mutator = mutator
        self.mutation_count: int = mutation_count

        self.outcome_list: List[str] = []

        self.chosen_seed = None
        self.reset()

    def reset(self) -> None:
        """"Reset the initial population, seed index, coverage information"""
        self.coverages_seen = set()
        self.population = list(map(lambda x: Seed(x), self.seeds))
        self.seed_index: int = 0

    def create_candidate(self) -> str:
        """Returns an input generated by fuzzing a seed in the population"""
        seed = self.schedule.choose(self.population)
        seed.chosen_count += 1
        self.chosen_seed = seed

        # Stacking: Apply multiple mutations to generate the candidate
        candidate = deepcopy(seed.data)
        num_mutations = random.randint(1, MUTATION_COUNT)
        for _ in range(num_mutations):
            candidate = self.mutator.mutate(candidate)
        return candidate

    def fuzz(self, inp: Any) -> ElementTree:
        """Returns first each seed once and then generates new inputs"""
        if self.seed_index < len(self.seeds):
            # Still seeding
            self.inp = self.seeds[self.seed_index]
            self.chosen_seed = self.population[0]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()
        return self.inp
    
    def handle_feedback(self, new_coverage: frozenset, result: str, outcome: str, document: ElementTree):
        # Can check for new coverage or based on result
        # could count outcome messages even if false
        if new_coverage not in self.coverages_seen:
            # Add to seen coverage

            self.coverages_seen.add(new_coverage)

            # Make new seed
            seed = Seed(document)
            seed.coverage = self.runner.code_coverage
            seed.outcome = outcome
            seed.result = result

            # Administration
            self.population.append(seed)
            self.total_coverage = self.total_coverage.union(self.runner.code_coverage)

            # Write and log new file
            filename: str = "fuzzed_document_" + str(self.seed_index) + ".xml"
            document_path = join(self.population_path, filename)
            document.write(document_path, encoding="utf-8", xml_declaration=True)
            self.logger.log_crash(filename, result)
            seed.population_name = filename
            self.seed_index += 1


    def run(self) -> Tuple[Any, str]:
        # "" since it needs an input
        document: ElementTree = self.fuzz("")
        # Make new name
        filename: str = "fuzzed_document_" + str(self.seed_index) + ".xml"
        result, outcome, _ = self.runner.run(document, filename)
        new_coverage = frozenset(self.runner.code_coverage)
        self.handle_feedback(new_coverage, result, outcome, document)
        return result, outcome

    def multiple_runs(self, run_count: int, stats: bool) -> List[Tuple[Any, str]]:
        results = []
        result_num = 0
        code_block_total = 55
        for i in range(run_count):
            result = self.run()
            run_num = i + 1
            path_num = len(self.coverages_seen)
            if result[0] not in results:
                results.append(result[0])
                result_num += 1
            percent_coverage = len(self.total_coverage)/code_block_total * 100
            to_print = "Run: " + str(run_num) + " Paths: " + str(path_num)
            to_print += " Coverage: " + str(format(percent_coverage, '.2f')) + " %"
            if stats:
                print(to_print,  end='\r')

        # Filter results marked as "PASS"
        if self.verbose:
            for cov in self.coverages_seen:
                print(cov)
            print(len(self.population))

        # Print how many times each is chosen
        # for s in self.population:
        #    print(s.outcome, s.chosen_count)

        # TODO Better filter? Perhaps look at response from runner
        return [result for result in results if result[1] != "PASS"]

import random
from typing import Any, List, Tuple, Set
from xml.etree.cElementTree import ElementTree
from os.path import join
from copy import deepcopy

if __name__ == "__main__":
    from fuzzer import Fuzzer
else:
    from .fuzzer import Fuzzer

import sys
sys.path.append("..")
from mutators import Mutator
from runners import Runner
from loggers import FeedbackLogger
from utils import Seed
from scheduler import PowerSchedule
from config import MUTATION_COUNT, MAX_DICT


class GreyboxFuzzer(Fuzzer):
    def __init__(self,
                 seeds: List[ElementTree],
                 runner: Runner,
                 mutator: Mutator,
                 logger: FeedbackLogger,
                 schedule: PowerSchedule,
                 verbose: bool,
                 write_path: str,
                 mutation_count: int) -> None:

        # List of existing seeds
        self.seeds: List[Seed] = list(map(lambda x: Seed(x), seeds))

        # 
        self.seed_index: int = 0
        self.population: List[Seed] = []
        self.verbose: bool = verbose
        self.total_coverage = set()

        self.write_path: str = write_path
        self.schedule: PowerSchedule = schedule
        self.runner: Runner = runner
        self.logger: FeedbackLogger = logger
        self.mutator: Mutator = mutator
        self.mutation_count: int = mutation_count

        self.log_count = 0


        # Current dictionary over the amount
        self.current_dict: dict = {"SCHEMA": 0, "PASS": 0, "SCHEMATRON": 0, "UNKNOWN": 0, "FAIL": 0, "XML": 0}
        

        self.chosen_seed = None


    def reset(self) -> None:
        """"Reset the initial population, seed index, coverage information"""
        self.coverages_list: List[set] = []
        self.outcome_list: List[str] = []
        self.seed_index: int = 0

    def create_candidate(self) -> str:
        """Returns an input generated by fuzzing a seed in the population"""
        seed = self.schedule.choose(self.population)

        if seed.chosen_count == 6:
            if self.current_dict[seed.outcome] != 1:
                self.population.remove(seed)
                self.current_dict[seed.outcome] -= 1
        else:
            seed.chosen_count += 1
        self.chosen_seed = seed

        # Stacking: Apply multiple mutations to generate the candidate
        candidate = deepcopy(seed.data)
        num_mutations = random.randint(1, MUTATION_COUNT)
        for _ in range(num_mutations):
            candidate = self.mutator.mutate(candidate)
        return candidate

    def fuzz(self) -> ElementTree:
        """Returns first each seed once and then generates new inputs"""
        if self.seed_index < len(self.seeds):
            # Still seeding
            self.chosen_seed = self.seeds[self.seed_index]
            self.inp = self.chosen_seed.data
        else:
            # Mutating
            self.inp = self.create_candidate()
        return self.inp
    
    def add_to_population(self, result: str, outcome: str, document: ElementTree):
        # Make new seed
        seed = Seed(document)
        seed.coverage = self.runner.code_coverage
        seed.outcome = outcome
        seed.result = result

        # Administration
        self.population.append(seed)
        self.total_coverage = self.total_coverage.union(self.runner.code_coverage)

        # Write and log new file
        # filename: str = "fuzzed_document_" + str(self.seed_index) + ".xml"
        # document_path = join(self.population_path, filename)
        # document.write(document_path, encoding="utf-8", xml_declaration=True)
        # self.logger.log_crash(filename, result)
        
        seed.population_name = outcome
        self.seed_index += 1

    def only_log(self, result: str, outcome: str, document: ElementTree):
        # Write and log new file
        filename: str = outcome + "-" + str(self.log_count) + ".xml"
        self.log_count += 1
        document_path = join(self.write_path, filename)
        document.write(document_path, encoding="utf-8", xml_declaration=True)
        self.logger.log_crash(filename, result)
    
    def handle_feedback(self, result: str, outcome: str, document: ElementTree):
        if self.current_dict[outcome] < MAX_DICT[outcome]:
            self.add_to_population(result, outcome, document)
            self.current_dict[outcome] += 1
        else:
            self.seed_index += 1

    def run(self) -> Tuple[Any, str]:
        # "" since it needs an input
        document: ElementTree = self.fuzz()
        # Make new name
        filename: str = "fuzzed_document_" + str(self.seed_index) + ".xml"
        result, outcome = self.runner.run(document, filename)
        new_coverage = frozenset(self.runner.code_coverage)
        self.handle_feedback(result, outcome, document)
        return result, outcome

    def multiple_runs(self, run_count: int, stats: bool) -> List[Tuple[Any, str]]:
        results = []
        code_block_total = 55
        try:
            for i in range(1, run_count + 1):
                result , _ = self.run()
                run_num = i
                pop_count = sum(self.current_dict.values())
                percent_coverage = len(self.total_coverage)/code_block_total * 100
                to_print = "Run: " + str(run_num) + " Population count: " + str(pop_count)
                to_print += " Coverage: " + str(format(percent_coverage, '.2f')) + " %"
                if stats:
                    print(to_print,  end='\r')
        except KeyboardInterrupt:
            print("Program terminated manually, writing population, do not stop it")
            for seed in self.population:
                self.only_log(seed.result, seed.outcome, seed.data)

        
        # Filter results marked as "PASS"
        if self.verbose:
            for cov in self.coverages_list:
                print(cov)
            print(len(self.population))

        # Write the population to fuzzed documents
        for seed in self.population:
            self.only_log(seed.result, seed.outcome, seed.data)

        # TODO Better filter? Perhaps look at response from runner
        return [result for result in results if result[1] != "PASS"]

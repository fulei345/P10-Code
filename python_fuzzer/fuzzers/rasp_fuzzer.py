from typing import Any, List, Tuple
import random

if __name__ == "__main__":
    from fuzzer import Fuzzer
else:
    from .fuzzer import Fuzzer

import sys
sys.path.append("..")
from mutators import PacketMutator
from runners import RaspRunner
from loggers import SimpleLogger


class RaspFuzzer(Fuzzer):
    def __init__(self,
                 seed,
                 runner: RaspRunner,
                 mutator: PacketMutator,
                 logger: SimpleLogger,
                 verbose: bool,
                 mutation_count: int) -> None:

        self.seed: seed
        self.seed_length: int = len(self.seed)
        self.seed_index: int = 0
        self.population = []

        self.verbose: bool = verbose

        self.runner: RaspRunner = runner
        self.logger: SimpleLogger = logger
        self.mutator: PacketMutator = mutator
        self.mutation_count: int = mutation_count

    def reset(self) -> None:
        self.population = []
        self.seed_index = 0

    def fuzz(self, document):
        random_range = random.randint(1, self.mutation_count)
        for _ in range(random_range):
            document = self.mutator.mutate(document)
        return document

    def choose_candidate(self) -> Any:
        if len(self.seed) > 0:
            candidate = self.seed[self.seed_index]
            self.seed_index += 1
            self.population.append(candidate)
            return candidate
        else:
            index: int = random.randint(0, len(self.population)-1)
            candidate = self.population[index]
            return candidate

    # TODO: Update below function when we have StateMachine and Runner working
    def run(self) -> Tuple[Any, str]:
        pass

    def multiple_runs(self, run_count: int) -> List[Tuple[Any, str]]:
        # TODO Filter so only crashes are returned if we want to run millions of iterations?
        return [self.run() for _ in range(run_count)]


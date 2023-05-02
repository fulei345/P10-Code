from typing import List, Sequence, Dict
import random
import sys
sys.path.append("..")
from utils import Seed
from config import WEIGHTED_PS

class PowerSchedule:
    """Define how fuzzing time should be distributed across the population."""

    def __init__(self) -> None:
        """Constructor"""
        self.path_frequency: Dict = {}

    def assignEnergy(self, population: Sequence[Seed]) -> None:
        """Assigns Schema 1, Valid 3 and else 2"""
        if WEIGHTED_PS:
            for seed in population:
                if seed.result.find("Schema"):
                    seed.energy = 1
                else:
                    if seed.outcome == "PASS":
                        seed.energy = 3
                    else:
                        seed.energy = 2
        else:
            # 1 to each
            for seed in population:
                seed.energy = 1
    def normalizedEnergy(self, population: Sequence[Seed]) -> List[float]:
        """Normalize energy"""
        energy = list(map(lambda seed: seed.energy, population))
        sum_energy = sum(energy)  # Add up all values in energy
        assert sum_energy != 0
        norm_energy = list(map(lambda nrg: nrg / sum_energy, energy))
        return norm_energy

    def choose(self, population: Sequence[Seed]) -> Seed:
        """Choose weighted by normalized energy."""
        self.assignEnergy(population)
        norm_energy = self.normalizedEnergy(population)
        seed: Seed = random.choices(population, weights=norm_energy)[0]
        return seed

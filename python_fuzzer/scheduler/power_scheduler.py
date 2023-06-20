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
        """Assigns energy to the seeds"""
        good_list: List[str] = ["FAIL", "PASS", "SCHEMATRON", "UNKNOWN"]
        # if outcome of a seed is FAIL, PASS, SCHEMATRON, or UNKNOWN assign energy to 5, else 1
        if WEIGHTED_PS:
            for seed in population:
                set_high: bool = False
                for i in good_list:
                    if seed.outcome == i:
                        seed.energy = 5
                        set_high = True
                if not set_high:
                    seed.energy = 1
        else:
            # 1 to each
            for seed in population:
                seed.energy = 1

    def normalizedEnergy(self, population: Sequence[Seed]) -> List[float]:
        """Normalize energy"""
        energy: List[float] = list(map(lambda seed: seed.energy, population))
        sum_energy: float = sum(energy)  # Add up all values in energy
        assert sum_energy != 0
        norm_energy: List[float] = list(map(lambda nrg: nrg / sum_energy, energy))
        return norm_energy

    def choose(self, population: Sequence[Seed]) -> Seed:
        """Choose weighted by normalized energy."""
        #assign
        self.assignEnergy(population)
        #normalize
        norm_energy: List[float] = self.normalizedEnergy(population)
        # make weigthed choice
        seed: Seed = random.choices(population, weights=norm_energy)[0]
        return seed

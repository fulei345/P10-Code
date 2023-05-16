

# Number of mutations done before sending
MUTATION_COUNT = 5

# If power scheduler should use weighted energy
WEIGHTED_PS = True

# Pobability for being inserted at same index, else at random posistion through the whole document
DUPLICATE_PROB = 0.95

# The number of times that seed is send before the seeds is getting replaced
REPLACE_COUNT = 10

# Max number of different seed type in population
MAX_DICT = {"SCHEMA": 5, "PASS": 5, "SCHEMATRON": 15, "UNKNOWN": 50, "FAIL": 50, "XML": 5}

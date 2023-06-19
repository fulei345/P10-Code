

# Number of mutations done before sending
MUTATION_COUNT = 5

# If power scheduler should use weighted energy
WEIGHTED_PS = True

# Pobability for being inserted at same index, else at random posistion through the whole document
PLACEMENT_PROB = 0.95

# probability of an optional field being made
OPT_PROB = 0.5

# The number of times that seed is send before the seeds is getting replaced
REPLACE_COUNT = 10

# maximal recursion depth when creating invoice classes
MAX_RECUR_DEPTH = 30

# Probability of following the correct type
TYPE_PROB = 0.80

# Max number of different seed type in population
MAX_DICT = {"SCHEMA": 5, "PASS": 5, "SCHEMATRON": 15, "UNKNOWN": 50, "FAIL": 75, "XML": 5}

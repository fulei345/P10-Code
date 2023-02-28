from parsers import DocumentParser
from loggers import SimpleLogger
from fuzzers import RaspFuzzer
from runners import RaspRunner
from mutators import DocumentMutator

import os
import argparse
from typing import List


# TODO Add types to everything without and change existing types

def main(verbose: bool) -> None:
    # Get current working directory to create folders
    cwd_path: str = os.getcwd()
    if not cwd_path.endswith("python_fuzzer"):
        cwd_path = os.path.join(cwd_path, "python_fuzzer")

    # Initialize the logger
    # Maybe used for logging the good files that make it crash
    logger_path: str = os.path.join(cwd_path, "log_files")
    log: SimpleLogger = SimpleLogger(logger_path, verbose)

    # Initialize the runner
    process_path: str = os.path.join(cwd_path, "executables", "ClientExample")
    run: RaspRunner = RaspRunner(log, process_path, verbose)

    # Parse OIOUBL documents
    document_path: str = os.path.join(cwd_path, "documents")
    parser: DocumentParser = DocumentParser(document_path, verbose)
    seed = parser.load_seed()

    # Initialize the mutator
    mut: DocumentMutator = DocumentMutator(verbose)

    # Initialize and run the fuzzer
    fuzz: RaspFuzzer = RaspFuzzer(seed, run, mut, log, verbose, mutation_count=1)
    result = fuzz.multiple_runs(run_count=len(seed))
    print(result)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description="Arguments for fuzzing harness")

    p.add_argument("--verbose",
                   default=False,
                   action="store_true",
                   help="Use this flag if fuzzing process information should be printed to terminal")

    args = p.parse_args()

    main(args.verbose)

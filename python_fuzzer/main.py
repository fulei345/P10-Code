from parsers import DocumentParser
from loggers import FeedbackLogger
from fuzzers import RaspFuzzer, GreyboxFuzzer
from runners import RaspRunner
from mutators import DocumentMutator
from scheduler import  PowerSchedule
from utils import Seed, Ddos

import os
import argparse
from typing import List
from xml.etree.ElementTree import Element, ElementTree, parse, ParseError

# TODO Add types to everything without and change existing types

def main(verbose: bool, ddos: bool) -> None:
    if ddos:
        cwd_path: str = os.getcwd()
        if not cwd_path.endswith("python_fuzzer"):
            cwd_path = os.path.join(cwd_path, "python_fuzzer")
        process_path: str = os.path.join(cwd_path, "executables", "ClientExample")
        document_path: str = os.path.join(process_path, "Resources", "xml", "ProductionUddi", "OIOUBL_Invoice_v2p2.xml")
        dosser: Ddos = Ddos()
        dosser.generate(full_file_path=document_path)
        dosser.run(process_path)
    else:
        # Get current working directory to create folders
        cwd_path: str = os.getcwd()
        if not cwd_path.endswith("python_fuzzer"):
            cwd_path = os.path.join(cwd_path, "python_fuzzer")
    
        # Initialize the logger
        # Maybe used for logging the good files that make it crash
        logger_path: str = os.path.join(cwd_path, "log_files")
        log: FeedbackLogger = FeedbackLogger(logger_path, verbose)
    
        # Initialize the runner
        process_path: str = os.path.join(cwd_path, "executables", "ClientExample")
        run: RaspRunner = RaspRunner(log, process_path, verbose)
    
        # Parse OIOUBL documents
        document_path: str = os.path.join(cwd_path, "documents", "existing")
        parser: DocumentParser = DocumentParser(document_path, verbose)
        corpus_str, corpus = parser.load_corpus()
    
        # Initialize the mutator
        mut: DocumentMutator = DocumentMutator(verbose)
    
        population_path: str = os.path.join(cwd_path, "documents", "population")
        # Initialize and run the fuzzer
        # fuzz: RaspFuzzer = RaspFuzzer(corpus_str, run, mut, log, verbose, parser, document_path, mutation_count=1)
        # result = fuzz.multiple_runs(run_count=3)
        # print(result)
    
        # Greybox fuzzer
        fuzz: GreyboxFuzzer = GreyboxFuzzer(corpus, run, mut, log, PowerSchedule(), verbose, population_path, mutation_count=1)
        result = fuzz.multiple_runs(run_count=1000000)
        # print(result)

if __name__ == '__main__':
    p = argparse.ArgumentParser(description="Arguments for fuzzing harness")

    p.add_argument("--verbose",
                   default=False,
                   action="store_true",
                   help="Use this flag if fuzzing process information should be printed to terminal")

    p.add_argument("--ddos",
                   default=False,
                   action="store_true",
                   help="Use this flag if you want to ddos the ClientExample")

    args = p.parse_args()

    main(args.verbose, args.ddos)

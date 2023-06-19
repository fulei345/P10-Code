# P10-Code

Python 3.10 or above is required to be able to run all of the code

This repository contains the code for OIOFuzz developed for the master thesis "OIOFuzz: A Guided Model-based Blackbox Fuzzer for OIORASP Schematron Validation".

OIOFuzz is a Guided Model-based Black-box fuzzer.
The fuzzer is in the python_fuzzer folder and the working-rasp-files has files for setting up the ClientExample and the HttpEndpointExample.
Before the fuzzer can be run the ClientExample need to be compiled and its files need to be put into the executable folder.

The existing folder in documents is for the initial corpus, which contains OIORASP invoice example documents.

OIOFuzz is run by running `main.py` which can take some optional flags, which is `--verbose` and `--stats`, for printing all information or just printing the stats regarding the fuzzing process respectively.

After the fuzzing process the final population is written to the fuzzed_documents folder in documents and their returned message is in log_files, with the same name.

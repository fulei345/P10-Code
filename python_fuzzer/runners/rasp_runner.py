from typing import Tuple
from subprocess import run
from os import getcwd
from os.path import join
from xml.etree.cElementTree import ElementTree
from re import findall
import traceback
import os

if __name__ == "__main__":
    from runner import Runner
else:
    from .runner import Runner

import sys
sys.path.append("..")
from loggers import Logger


class RaspRunner(Runner):
    def __init__(self, log: Logger, path: str, verbose: bool) -> None:
        self.PASS: str = 'PASS'
        self.FAIL: str = 'FAIL'
        self.SCHEMA: str = 'SCHEMA'
        self.SCHEMATRON: str = 'SCHEMATRON'
        self.XML: str = 'XML'
        self.UNKNOWN: str = 'UNKNOWN'

        self.logger: Logger = log
        self.executable_path: str = path
        self.verbose: bool = verbose
        self.code_coverage = []

    def run(self, document: ElementTree, filename: str) -> Tuple[str, str]:
        #make path for document and write the document there, then run process with path provided
        document_path = join(self.executable_path, "Resources", "xml", "ProductionUddi", filename)
        document.write(document_path, encoding="utf-8", xml_declaration=True)
        message, outcome = self.start_process(document_path)
        #remove file from executable folder
        os.remove(document_path)
        return message, outcome

    def start_process(self, doc_path: str) -> Tuple[str, str]:
        # Initialize coverage if something goes wrong
        self.code_coverage = {}
        try:
            # run client example with specified document path
            process = run(["dk.gov.oiosi.samples.ClientExample.exe", doc_path],
                          shell=True,
                          cwd=self.executable_path,
                          timeout=30,
                          capture_output=True)

            # if the process failed during run, handles the error
            if process.returncode != 0:
                standard_error = process.stderr.decode("utf-8", errors="replace")
                if self.verbose:
                    print(standard_error)
                return standard_error, self.FAIL
            # if it suceeded, handle feedback
            elif process.returncode == 0:
                # handle decode error for ø, æ and å by replacing them
                standard_out = process.stdout.decode("utf-8", errors="replace")
                return self.handle_feedback(standard_out)
        except Exception as err:
            traceback.print_exc()
            return str(traceback.format_exception(err)), self.FAIL

    def handle_feedback(self, standard_out: str) -> Tuple[str, str]:
        # Find code blocks for code coverage
        self.code_coverage = findall(r"BLOCK:\d+", standard_out)

        if self.verbose:
            print(standard_out)

        if "Response received" in standard_out:
            # It was succesful
            return standard_out, self.PASS
        # It did not pass
        else:
            # list of known xml exception returned from client
            xml_list = ["NoDocumentTypeFoundFromXmlDocumentException",
                        "System.Xml.XmlException",
                        "SearchForDocumentTypeFromXmlDocumentFailedException",]

            if standard_out.find("ERROR") != -1:
                return standard_out, self.FAIL

            elif standard_out.find("Schema ") != -1:
                return standard_out, self.SCHEMA
            
            elif standard_out.find("Schematron") != -1:
                return standard_out, self.SCHEMATRON

            else:
                #checks if its one of the known xml exceptions
                for s in xml_list:
                    if s in standard_out:
                        return standard_out, self.XML
                #else its unknown
                return standard_out, self.UNKNOWN
            

if __name__ == '__main__':
    cwd_path = getcwd()
    # Get path to the folder of the ClientExample
    process_path: str = join(cwd_path, "..", "executables", "ClientExample")
    logger: Logger = Logger(cwd_path, True)
    runner: RaspRunner = RaspRunner(logger, process_path, True)

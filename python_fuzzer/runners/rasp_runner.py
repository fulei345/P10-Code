from typing import Any, Tuple, List
from subprocess import run
from os import getcwd
from os.path import join
from xml.etree.ElementTree import ElementTree
from re import search

if __name__ == "__main__":
    from runner import Runner
else:
    from .runner import Runner

import sys

sys.path.append("..")
from loggers import FeedbackLogger


class RaspRunner(Runner):
    def __init__(self, log: FeedbackLogger, path: str, verbose: bool) -> None:
        self.PASS: str = 'PASS'
        self.FAIL: str = 'FAIL'
        self.UNRESOLVED: str = 'UNRESOLVED'
        self.EXCEPTION: str = 'EXCEPTION'
        self.UNKNOWN: str = 'UNKNOWN'

        self.logger: FeedbackLogger = log
        self.ersp_nums: List[str] = []

        self.executable_path: str = path
        self.verbose: bool = verbose

    def run(self, document: ElementTree, filename: str) -> Tuple[Any, str]:
        document_path = join(self.executable_path, "Resources", "xml", "ProductionUddi", filename)
        document.write(document_path, encoding="utf-8", xml_declaration=True)
        code, message = self.start_process(document_path)
        return document, code

    def start_process(self, doc_path: str) -> Tuple[str, str]:
        try:
            # Input is the options chosen in the Client
            process = run(["dk.gov.oiosi.samples.ClientExample.exe", doc_path],
                          shell=True,
                          cwd=self.executable_path,
                          timeout=30,
                          capture_output=True)

            if process.returncode != 0:
                standard_error = process.stderr.decode("utf-8", errors="replace")
                if self.verbose:
                    print(standard_error)

                self.logger.log_crash(doc_path, standard_error)
                return self.FAIL, standard_error

            elif process.returncode == 0:
                # TODO find better way to handle decode error for ø (+ æ and å, i suppose)
                standard_out = process.stdout.decode("utf-8", errors="replace") 
                # finds the second instance of the substring, which is the start of the error message
                erro_index = standard_out.find("dk.gov.oiosi", standard_out.find("dk.gov.oiosi")+1)
                # Check if we found it
                if -1 != erro_index:
                    # Do some regex to see if new E-RSP
                    # Log if new, do not if not
                    fault_message = standard_out[erro_index:]
                    ersp_num = search(r" E-RSP\d+", fault_message)
                    if ersp_num.group(0) not in self.ersp_nums:
                        self.ersp_nums.append(ersp_num.group(0))
                        self.logger.log_crash(doc_path, fault_message)
                        if self.verbose:
                            print(fault_message)
                        # If it was an E-RSP fault
                        return self.EXCEPTION, fault_message
                    if self.verbose:
                        print(fault_message)
                    # If it was not E-RSP
                    return self.UNKNOWN, fault_message
                else:
                    if self.verbose:
                        print(standard_out)
                    # If there is no error
                    return self.PASS, standard_out
        except:
            # TODO handle this better
            pass


if __name__ == '__main__':
    cwd_path = getcwd()
    # Get path to the folder of the ClientExample
    process_path: str = join(cwd_path, "..", "executables", "ClientExample")
    logger: FeedbackLogger = FeedbackLogger(cwd_path, True)
    runner: RaspRunner = RaspRunner(logger, process_path, True)

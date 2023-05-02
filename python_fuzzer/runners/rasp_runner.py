from typing import Any, Tuple, List
from subprocess import run
from os import getcwd
from os.path import join
from xml.etree.cElementTree import ElementTree
from re import search, findall
import traceback

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
        self.code_coverage = []

        # Just for E-RSP15324 and returncode not zero
        self.count = 0 

    def run(self, document: ElementTree, filename: str) -> Tuple[Any, str, List[str]]:
        document_path = join(self.executable_path, "Resources", "xml", "ProductionUddi", filename)
        document.write(document_path, encoding="utf-8", xml_declaration=True)
        message, code, code_coverage = self.start_process(document_path)
        return message, code, code_coverage

    def start_process(self, doc_path: str) -> Tuple[str, str, List[str]]:
        # Initialize coverage if something goes wrong
        self.code_coverage = {}
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
                outcome = self.FAIL + str(self.count)
                return standard_error, outcome, []

            elif process.returncode == 0:
                # TODO find better way to handle decode error for ø (+ æ and å, i suppose)
                standard_out = process.stdout.decode("utf-8", errors="replace")
                return self.handle_feedback(standard_out)
        except Exception:
            traceback.print_exc()
            return str(traceback.format_exception()), self.FAIL, []

    def handle_feedback(self, standard_out: str) -> Tuple[str, str, List[str]]:
        # Find code blocks for code coverage
        self.code_coverage = findall(r"BLOCK:\d+", standard_out)

        # finds the second instance of the substring, which is the start of the error message
        erro_index = standard_out.find("dk.gov.oiosi", standard_out.find("dk.gov.oiosi") + 1)

        # Check if we found it the start of an error
        if -1 != erro_index:

            # Find the fault message in the standard out
            fault_message = standard_out[erro_index:]

            # Regex to find E-RSP num
            ersp_num = findall(r"E-RSP\d+", fault_message)
            if len(ersp_num) > 1:
                # Log forskellige, hvis der er flere
                if ersp_num[1] == "E-RSP15324":
                    outcome = "E-RSP15324-" + str(self.count)
                    self.count += 1
                    return fault_message, outcome, self.code_coverage

            # If it is E-RSP and not already seen number
            if len(ersp_num) > 0 and ersp_num[0] not in self.ersp_nums:
                self.ersp_nums.append(ersp_num[0])

                ## F fault code
                # f_num = search(r"\[F-\w+\]", fault_message)
                # if f_num != None and f_num.group(0) not in self.ersp_nums:
                # self.ersp_nums.append(f_num.group(0))

                if self.verbose:
                    print(fault_message)

                # If it was an E-RSP fault
                return fault_message, ersp_num[0], self.code_coverage

            if self.verbose:
                print(fault_message)
            return fault_message, self.UNKNOWN, self.code_coverage

        else:
            if self.verbose:
                print(standard_out)
            # If we did not find any error
            return standard_out, self.PASS, self.code_coverage



if __name__ == '__main__':
    cwd_path = getcwd()
    # Get path to the folder of the ClientExample
    process_path: str = join(cwd_path, "..", "executables", "ClientExample")
    logger: FeedbackLogger = FeedbackLogger(cwd_path, True)
    runner: RaspRunner = RaspRunner(logger, process_path, True)

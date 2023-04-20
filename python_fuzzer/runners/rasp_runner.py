from typing import Any, Tuple, List
from subprocess import run
from os import getcwd
from os.path import join
from xml.etree.ElementTree import ElementTree
from re import search, findall

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

    def run(self, document: ElementTree, filename: str) -> Tuple[Any, str, List[str]]:
        document_path = join(self.executable_path, "Resources", "xml", "ProductionUddi", filename)
        document.write(document_path, encoding="utf-8", xml_declaration=True)
        message, code, code_coverage = self.start_process(document_path)
        return message, code, code_coverage

    def start_process(self, doc_path: str) -> Tuple[str, str, List[str]]:
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
                return standard_error, self.FAIL, []

            elif process.returncode == 0:
                # TODO find better way to handle decode error for ø (+ æ and å, i suppose)
                standard_out = process.stdout.decode("utf-8", errors="replace")
                return self.handle_feedback(standard_out, doc_path)
        except Exception as e:
            # TODO handle this better
            print(e)
            return "", self.FAIL, []

    def handle_feedback(self, standard_out: str, doc_path: str) -> Tuple[str, str, List[str]]:
        # Find code blocks for code coverage
        self.code_coverage = findall(r"BLOCK:\d+", standard_out)

        # finds the second instance of the substring, which is the start of the error message
        erro_index = standard_out.find("dk.gov.oiosi", standard_out.find("dk.gov.oiosi") + 1)

        # Check if we found it the start of an error
        if -1 != erro_index:

            # Find the fault message in the standard out
            fault_message = standard_out[erro_index:]

            # Regex to find E-RSP num
            ersp_num = search(r" E-RSP\d+", fault_message)

            # If it is E-RSP and not already seen number
            if ersp_num != None and ersp_num.group(0) not in self.ersp_nums:
                self.ersp_nums.append(ersp_num.group(0))

                ## F fault code
                # f_num = search(r"\[F-\w+\]", fault_message)
                # if f_num != None and f_num.group(0) not in self.ersp_nums:
                # self.ersp_nums.append(f_num.group(0))

                # Should be removed, only for compatibility med OG fuzzer
                self.logger.log_crash(doc_path, fault_message)
                if self.verbose:
                    print(fault_message)

                # If it was an E-RSP fault
                return fault_message, self.EXCEPTION, self.code_coverage

            if self.verbose:
                print(fault_message)
            # If it was not E-RSP
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

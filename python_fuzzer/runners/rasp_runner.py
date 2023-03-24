from typing import Any, Tuple, Callable
from subprocess import run
from os import getcwd
from os.path import join
from xml.etree.ElementTree import ElementTree

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

        self.logger: FeedbackLogger = log

        self.executable_path: str = path
        self.verbose: bool = verbose
        self.index: int = 1

    def run(self, document: ElementTree) -> Tuple[Any, str]:
        document_path = join(self.executable_path, "Resources", "xml", "ProductionUddi", ("fuzzed_document_" + str(self.index) + ".xml"))
        document.write(document_path, encoding="utf-8", xml_declaration=True)
        code, message = self.start_process(document_path)
        # TODO Write ElementTree to XML file and send that to the ClientExample
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
                if self.verbose:
                    print(process.stderr.decode("utf-8"))

                self.logger.log_crash(process.stderr)
            else:
                standard_out = process.stdout.decode("utf-8", errors="replace") 
                #TODO find better way to handle decode error for ø (+ æ and å, i suppose)
                index = standard_out.find("Exception")
                if -1 != index:
                    # This just means that we found the fault
                    fault_message = standard_out[index:]
                    self.logger.log_crash(doc_path, fault_message)
                    print(fault_message)
                    return self.FAIL, fault_message

                if self.verbose:
                    print(standard_out)
            return self.PASS, ""
        except:
            # TODO handle this better
            self.logger.log_crash(doc_path, process.stdout)
            return self.PASS, ""
            pass


if __name__ == '__main__':
    cwd_path = getcwd()
    # Get path to the folder of the ClientExample
    process_path: str = join(cwd_path, "..", "executables", "ClientExample")
    logger: FeedbackLogger = FeedbackLogger(cwd_path, True)
    runner: RaspRunner = RaspRunner(logger, process_path, True)

    # Test that python does not crash
    for _ in range(1):
        print(_)
        runner.start_process()

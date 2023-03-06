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
from loggers import SimpleLogger


class RaspRunner(Runner):
    def __init__(self, log: SimpleLogger, path: str, verbose: bool) -> None:
        self.PASS: str = 'PASS'
        self.FAIL: str = 'FAIL'
        self.UNRESOLVED: str = 'UNRESOLVED'

        self.logger: SimpleLogger = log

        self.executable_path: str = path
        self.verbose: bool = verbose

    def run(self, document: ElementTree) -> Tuple[Any, str]:
        document_path = join(self.executable_path, "Resources", "xml", "ProductionUddi")
        document.write(join(document_path,"OIOUBL_Invoice_v2p2.xml"))
        code, message = self.start_process()
        # TODO Write ElementTree to XML file and send that to the ClientExample
        return document, code

    def start_process(self) -> tuple[str, str]:
        try:
            # Input is the options chosen in the Client
            process = run(["dk.gov.oiosi.samples.ClientExample.exe"],
                          shell=True,
                          cwd=self.executable_path,
                          timeout=30,
                          capture_output=True)

            if process.returncode != 0:
                if self.verbose:
                    print(process.stderr.decode("utf-8"))

                self.logger.log_crash(process.stderr)
            else:
                standard_out = process.stdout.decode("utf-8")
                if -1 != standard_out.find("FaultReturnedException"):
                    # This just means that we found the same fault
                    print("Fault")
                    return self.FAIL, standard_out

                if self.verbose:
                    print(standard_out)
        except:
            # TODO handle this better
            pass


if __name__ == '__main__':
    cwd_path = getcwd()
    # Get path to the folder of the ClientExample
    process_path: str = join(cwd_path, "..", "executables", "ClientExample")
    logger: SimpleLogger = SimpleLogger(cwd_path, True)
    runner: RaspRunner = RaspRunner(logger, process_path, True)

    # Test that python does not crash
    for _ in range(3):
        print(_)
        runner.start_process()

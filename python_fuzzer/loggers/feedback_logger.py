from typing import Any
from shutil import copy2
from os.path import split, join
from os import getcwd

if __name__ == "__main__":
    from logger import Logger
else:
    from .logger import Logger


class FeedbackLogger(Logger):
    def __init__(self, path: str, verbose: bool) -> None:
        self.path: str = path
        self.verbose: bool = verbose

    def log_crash(self, inp: Any, out: Any) -> None:
        """
        Logs the crash in log_files, (and copies crashing files to where ??)
        :input: inp name of the OIOUBL document to be copied, out feedback
        """
        # Write a crash file with the file name and write crashing file

        filename = split(inp)[-1]
        fuzzed_path: str = join(getcwd(), "documents", "fuzzed_documents")
        # Copy file from
        copy2(inp, join(fuzzed_path, filename))


        pass

from typing import Any
from shutil import copy2, copyfile
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
        cwd_path = getcwd()

        # Copy fuzzed document from ClientExample
        filename = split(inp)[-1]
        fuzzed_path: str = join(cwd_path, "documents", "fuzzed_documents")
        copyfile(inp, join(fuzzed_path, filename))

        # Line with name and divider and the error message
        log_name = join(self.path,filename + ".txt")
        with open(log_name, "w") as file:
            # set a list of lines to add:
            lines = [filename + "\n", "-------------------------------------------------\n", out]
            file.writelines(lines)

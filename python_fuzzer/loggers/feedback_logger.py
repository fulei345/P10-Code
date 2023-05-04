from typing import Any
from shutil import copy2, copyfile
from os.path import split, join
from os import getcwd

if __name__ == "__main__":
    from logger import Logger
else:
    from .logger import Logger


class FeedbackLogger(Logger):
    def __init__(self, log_path: str, verbose: bool) -> None:
        self.log_path: str = log_path
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
        with open(log_name, "w", encoding="utf-8") as file:
            # set a list of lines to add:
            message = out.splitlines()
            message = [line + "\n" for line in message]
            file.write(filename + "\n")
            file.write("-------------------------------------------------\n")
            file.writelines(message)

    def log_crash(self, filename: str, out: Any) -> None:
        """
            Logs the crash in log_files, (and copies crashing files to where ??)
            :input: inp name of the OIOUBL document to be copied, out feedback
            """
        # Line with name and divider and the error message
        log_name = join(self.log_path, filename + ".txt")
        with open(log_name, "w", encoding="utf-8") as file:
            # set a list of lines to add:
            message = out.splitlines()
            message = [line + "\n" for line in message]
            file.write(filename + "\n")
            file.write("-------------------------------------------------\n")
            file.writelines(message)

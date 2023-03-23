from typing import Any

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


        pass

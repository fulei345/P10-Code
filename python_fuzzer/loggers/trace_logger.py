from typing import Any

if __name__ == "__main__":
    from logger import Logger
else:
    from .logger import Logger


class TraceLogger(Logger):
    def __init__(self, path: str, verbose: bool) -> None:
        self.path: str = path
        self.verbose: bool = verbose

    def log_crash(self, inp: Any, out: Any) -> None:
        """
        Logs the crash in log_files (copy trace), (and copies crashing files to where ??)
        :input: inp name of the OIOUBL document to be copied, out ´(idk what out should be)
        """
        pass

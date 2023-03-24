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
        Idk what we should do, to combine a trace with a document seems a lot
        Like make a log document, and save the traces and documents
        """
        pass

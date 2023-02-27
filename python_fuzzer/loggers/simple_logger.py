from typing import Any

from .logger import Logger


class SimpleLogger(Logger):
    def __init__(self, path: str, log_optional: bool, verbose: bool) -> None:
        self.path: str = path
        self.log_optional: bool = log_optional
        self.verbose: bool = verbose

    def log_traffic(self, document) -> None:
        # TODO: Implement
        pass

    def log_crash(self, inp: Any) -> None:
        # TODO: Implement
        pass

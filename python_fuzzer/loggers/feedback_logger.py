from typing import Any

if __name__ == "__main__":
    from logger import Logger
else:
    from .logger import Logger


class FeedbackLogger(Logger):
    def __init__(self, path: str, verbose: bool) -> None:
        self.path: str = path
        self.verbose: bool = verbose

    def log_crash(self, inp: Any) -> None:
        # TODO: Implement
        pass

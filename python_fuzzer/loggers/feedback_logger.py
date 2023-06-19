from typing import Any
from os.path import join

if __name__ == "__main__":
    from logger import Logger
else:
    from .logger import Logger


class FeedbackLogger(Logger):
    def __init__(self, log_path: str, verbose: bool) -> None:
        self.log_path: str = log_path
        self.verbose: bool = verbose

    def log(self, filename: str, out: str) -> None:
        """
            Logs the feedback in log_files
            :input: filename of the file resulting in the output, out: feedback message
            """
        # Line with name, a divider, and the error message
        log_name = join(self.log_path, filename + ".txt")
        with open(log_name, "w", encoding="utf-8") as file:
            # split the lines of feedback and make newlines
            message = out.splitlines()
            message = [line + "\n" for line in message]
            
            file.write(filename + "\n")
            file.write("-------------------------------------------------\n")
            file.writelines(message)

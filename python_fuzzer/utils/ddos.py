from subprocess import run


class Ddos:
    """Class for ddsosing the ClientExample, maybe server in future"""

    def __init__(self) -> None:
        pass

    def generate(self, full_file_path: str, size=30000000) -> None:
        with open(full_file_path, 'w') as f:
            for i in range(size):
                f.write("<A" + str(i) + ">\n")

    # This is going to result in a message with that A(your num) does not have a close if it stops
    def run(self, executable_path: str ) -> None:
        try:
            # Input is the options chosen in the Client
            process = run("dk.gov.oiosi.samples.ClientExample.exe",
                shell=True,
                cwd=executable_path,
                capture_output=True)
            print(process.stdout)
        except Exception as e:
            # TODO handle this better
            print(e)


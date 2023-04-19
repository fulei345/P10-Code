import random
from datetime import date, time
import string
import sys

# Just an encapsulation of the methods
class TypeGenerator:

    @staticmethod
    def make_string() -> str:

        length = random.randint(0, 100)

        # random string of legnth composed of printable string chararcters (letters, digits, punctuation, whitespace) - alternatively string.ascii_letters + string.digits (+string.punctuation)
        text = ''.join(random.choice(string.printable) for _ in range(length))

        return text

    @staticmethod
    def make_int() -> str:
        text = random.randint(0, sys.maxsize)

        return str(text)

    @staticmethod
    def make_float() -> str:
        text = random.uniform(0, sys.maxsize)

        return str(text)

    @staticmethod
    def make_bool() -> str:
        if random.random() < 0.5:
            text = "false"
        else:
            text = "true"

        return text

    @staticmethod
    def make_time() -> str:
        # create time with random values, first argument is hours, second argument is minutes, and last argument is seconds
        text = time(random.randint(0, 23), random.randint(0, 60), random.randint(0, 60))

        return str(text)

    @staticmethod
    def make_date() -> str:
        # create date with random values, first argument is year with the range for datetime modules minyear and maxyear, second argument is month, and last argument is day
        text = date(random.randint(1, 9999), random.randint(1, 12), random.randint(1, 31))

        return str(text)

import random
from datetime import date, time
import string
import sys

# Just an encapsulation of the methods
class TypeGenerator:

    @staticmethod
    def make_string() -> str:

        length = random.randint(0, 100)

        # random string of length composed of printable string chararcters (letters, digits, punctuation, whitespace) - alternatively string.ascii_letters + string.digits (+string.punctuation)
        # string.printable
        text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

        return text

    @staticmethod
    def make_char() -> str:

        text = '' + random.choice(string.printable)

        return text

    @staticmethod
    def make_int() -> str:
        text = random.randint(0, sys.maxsize)

        return str(text)

    @staticmethod
    def make_float() -> str:
        sign = random.choice(["-", "+"])
        first = TypeGenerator.make_int()
        second = TypeGenerator.make_int()
        text: str = sign + first + "." + second
        return text

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
        text = time(random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

        return str(text)

    @staticmethod
    def make_date() -> str:
        # create date with random values, first argument is year with the range for datetime modules minyear and maxyear, second argument is month, and last argument is day
        text = str(random.randint(1, 9999)) + "-" + str(random.randint(1, 12)) + "-" + str(random.randint(1, 31))

        return text

    @staticmethod
    def make_float_thousands() -> str:
        sign: str = random.choice(["-", "+"])
        commas: int = random.randint(1, 10)
        text: str = ""
        for i in range(commas):
            text = text + "000,"
        text = text + "000."
        text = sign + TypeGenerator.make_int() + text 
        return text

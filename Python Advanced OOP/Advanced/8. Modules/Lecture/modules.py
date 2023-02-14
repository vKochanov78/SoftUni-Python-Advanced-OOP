from pyfiglet import figlet_format
from math import log
import operator as op


def create_an_ascii_art(message):
    art = figlet_format(message)
    return art


def calculate_logarithm(number: int, base):
    if base == "natural":
        number = log(number)
    else:
        number = log(number, int(base))

    return f"{number:.2f}"


def draw_triangle(number: int):
    triangle = ""

    # The first part of the art.
    for i in range(1, number + 1):
        for j in range(1, i + 1):
            triangle += f"{j}"
        triangle += "\n"

    # The second part of the art
    for i in range(number, 0, -1):
        for j in range(1, i):
            triangle += f"{j}"
        triangle += "\n"

    return triangle


def operations(first_num, operator, second_num):
    first_num, second_num = int(first_num), int(second_num)

    valid_operators = {
        "+": op.add,
        "-": op.sub,
        "*": op.mul,
        "/": op.truediv,
        "^": op.xor,
    }

    result = valid_operators[operator](first_num, second_num)
    return f"{result:.2f}"


    # Fibonacci sequence
sequence_of_numbers = []
def create_sequence(number):

    sequence_of_numbers.clear()
    sequence_of_numbers.append(0)
    sequence_of_numbers.append(1)

    for _ in range(number - 2):
        sequence_of_numbers.append(
            sequence_of_numbers[-1] + sequence_of_numbers[-2]
        )

    return ' '.join(map(str, sequence_of_numbers))


def locate_number(number):
    if number in sequence_of_numbers:
        number_index = sequence_of_numbers.index(int(number))
        return f"The number - {number} is at index {number_index}"
    else:
        return f"The number - {number} is not in the sequence"

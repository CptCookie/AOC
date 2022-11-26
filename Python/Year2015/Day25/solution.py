import re


def get_table_number(x: int, y: int) -> int:
    result = (x * (x - 1) + y * (y - 3) + 2 * (x * y + 1)) / 2
    return int(result)


def get_number(x: int, y: int) -> int:
    number = 20151125
    for i in range(1, get_table_number(x, y)):
        number = (number * 252533) % 33554393
    return number


def solution_1(puzzle_input: str):
    y = re.search(r"row (\d+)", puzzle_input).groups()[0]
    x = re.search(r"column (\d+)", puzzle_input).groups()[0]

    return get_number(int(x), int(y))


def solution_2(puzzle_input: str):
    return None

from typing import List
import re


def valid_triangle(sides: List[int]):
    a, b, c = sorted(sides)
    return a + b > c


def number_valid_triange_col(values: List[int]):
    chunks = [values[i : i + 3] for i in range(0, len(values), 3)]
    return len([1 for n in chunks if valid_triangle(n)])


def solution_1(puzzle_input: str):
    values = []
    for line in puzzle_input.splitlines():
        values.append([int(n) for n in re.findall(r"\d+", line)])

    return len([1 for n in values if valid_triangle(n)])


def solution_2(puzzle_input: str):
    values = [int(n) for n in re.findall(r"\d+", puzzle_input)]
    return number_valid_triange_col(
        [n for n in values[0::3]]
        + [n for n in values[1::3]]
        + [n for n in values[2::3]]
    )
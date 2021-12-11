from statistics import median
from types import NoneType


OPENING = "([{<"
CLOSING = ")]}>"
POINTS_WRONG = {")": 3, "]": 57, "}": 1197, ">": 25137}
POINTS_MISSING = {"(": 1, "[": 2, "{": 3, "<": 4}


def parse_data(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.splitlines() if n != ""]


def first_closing_index(line):
    closings = []
    for c in CLOSING:
        if c in line:
            closings.append(line.index(c))

    if closings:
        return min(closings)


def parse_brackets(line: str, deleted_pairs=0) -> int:
    closing_pos = first_closing_index(line)

    if closing_pos:
        if OPENING.index(line[closing_pos - 1]) == CLOSING.index(line[closing_pos]):
            return parse_brackets(
                line[: closing_pos - 1] + line[closing_pos + 1 :], deleted_pairs + 1
            )
        else:
            return closing_pos + deleted_pairs * 2

    elif len(line) != 0:
        return line
    else:
        return None


def calc_points(line: str):
    points = 0
    for c in reversed(line):
        points *= 5
        points += POINTS_MISSING[c]
    return points


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    brackets = [parse_brackets(line) for line in data]
    points = [
        POINTS_WRONG[data[i][n]]
        for i, n in enumerate(brackets)
        if type(n) not in [str, NoneType]
    ]
    return sum(points)


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    brackets = [parse_brackets(line) for line in data]
    missing_brackets = [n for n in brackets if type(n) == str]
    points = sorted([calc_points(line) for line in missing_brackets])
    return points[int(len(points) / 2)]

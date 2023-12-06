import math
import operator
import re
from functools import reduce


def parse_individual(aoc_input: str) -> list[tuple[int, int]]:
    time, dist, *_ = aoc_input.splitlines()

    times = [int(n.group()) for n in re.finditer(r"\d+", time)]
    dists = [int(n.group()) for n in re.finditer(r"\d+", dist)]

    return list(zip(times, dists))


def parse_total(aoc_input: str) -> tuple[int, int]:
    time_str, dist_str, *_ = aoc_input.splitlines()

    time = int("".join(c for c in time_str if c.isdigit()))
    dist = int("".join(c for c in dist_str if c.isdigit()))

    return time, dist


def get_number_winning_moves(record):
    time, dist = record
    fix, root = time / 2, math.sqrt(time**2 / 4 - dist)
    solutions = (fix - root, fix + root)
    return math.ceil(max(solutions)) - math.ceil(min(solutions))


def solution_1(aoc_input: str) -> int:
    records = parse_individual(aoc_input)
    return reduce(operator.mul, (get_number_winning_moves(r) for r in records), 1)


def solution_2(aoc_input: str) -> int:
    record = parse_total(aoc_input)
    return get_number_winning_moves(record)

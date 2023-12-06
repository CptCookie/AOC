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


def get_num_win_moves(record: tuple[int, int]) -> int:
    time, dist = record
    start, end = 0, 0

    for hold in range(1, time):
        if hold * (time - hold) > dist and not start:
            start = hold

        if (time - hold) * hold > dist and not end:
            end = time - hold

        if start and end:
            return end - start + 1
    return 0


def solution_1(aoc_input: str) -> int:
    records = parse_individual(aoc_input)
    return reduce(operator.mul, (get_num_win_moves(r) for r in records), 1)


def solution_2(aoc_input: str) -> int:
    record = parse_total(aoc_input)
    return get_num_win_moves(record)

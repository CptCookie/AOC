import re
from typing import Optional


def parse_input(aoc_input: str) -> tuple[list[range], list[int]]:
    range_input, id_input = aoc_input.split("\n\n")
    ranges, ids = [], []
    range_pattern = r"(\d+)-(\d+)"

    for match in re.finditer(range_pattern, range_input):
        start, end = match.groups()
        ranges.append(range(int(start), int(end) + 1))

    ids = [int(n) for n in id_input.splitlines() if n != ""]

    return ranges, ids


def is_fresh(id: int, ranges: list[range]):
    return any(id in r for r in ranges)


def join_range(r1: range, r2: range) -> Optional[range]:
    """
    |------r1----xxx|
                |xxx---r2-------|
    -> range(r1.start, r2.stop)

    |---xxxr1xxx----|
       |xxxr2xxx|
    -> r1

    |------r1-------|
                        |------r2-------|
    -> None
    """

    if (r1.stop - 1) in r2 and r1.start not in r2:
        return range(r1.start, r2.stop)

    if (r2.stop - 1) in r1 and r2.start not in r1:
        return range(r2.start, r1.stop)

    if r2.start in r1 and (r2.stop - 1) in r1:
        return r1

    if r1.start in r2 and (r1.stop - 1) in r2:
        return r2

    return None


def reduce_ranges(ranges: list[range]) -> list[range]:
    new_rs = []
    for r1 in ranges:
        has_joined = False

        for i, r2 in enumerate(new_rs):
            if jr := join_range(r1, r2):
                new_rs[i] = jr
                has_joined = True
                break

        if not has_joined:
            new_rs.append(r1)

    return new_rs


def solution_1(aoc_input: str):
    ranges, ids = parse_input(aoc_input)
    return sum(1 for i in ids if is_fresh(i, ranges))


def solution_2(aoc_input: str):
    ranges, _ = parse_input(aoc_input)
    for _ in range(len(ranges)):
        reduced_ranges = reduce_ranges(ranges)
        if len(reduced_ranges) == len(ranges):
            return sum(len(r) for r in ranges)

        ranges = reduced_ranges

    return "ERROR"

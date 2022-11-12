from typing import List, Iterable, Tuple


def parse_data(puzzle_input: str) -> List[List[int]]:
    lines = []
    for l in puzzle_input.splitlines():
        if l != "":
            lines.append([int(e) for e in l.split("\t") if e not in (" ", "", None)])
    return lines


def get_divisables(it: List[int]) -> Tuple[int, int] | Tuple[None, None]:
    for index, a in enumerate(it):
        for b in it[index + 1 :]:
            if a % b == 0:
                return a, b
            if b % a == 0:
                return b, a
    return None, None


def solution_1(puzzle_input: str) -> int:
    data = parse_data(puzzle_input)
    return sum([max(line) - min(line) for line in data])


def solution_2(puzzle_input: str) -> int:
    data = parse_data(puzzle_input)
    s = .0
    for line in data:
        divident, divisor = get_divisables(line)
        if divisor is not None and divident is not None:
            s += divident / divisor
    return int(s)

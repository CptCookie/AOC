import collections
from itertools import islice
from typing import List


def parse_data(puzzle_input: str) -> List[str]:
    return [n for n in puzzle_input if n not in ["\n", " "]]


def sliding_window_of_2(iterable):
    it = iter(iterable)
    window = collections.deque(islice(it, 2), maxlen=2)
    if len(window) == 2:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def sliding_window_over_halve(iterable):
    it = iter(iterable)

    for n, x in enumerate(it):
        index = (len(iterable) / 2 + n) % len(iterable)
        yield x, iterable[int(index)]


def solution_1(puzzle_input: str):
    digits = parse_data(puzzle_input)
    return sum(int(l) for l, r in sliding_window_of_2(digits + digits[:1]) if l == r)


def solution_2(puzzle_input: str):
    digits = parse_data(puzzle_input)
    return sum(int(l) for l, r in sliding_window_over_halve(digits) if l == r)

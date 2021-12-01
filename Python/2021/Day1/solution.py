from typing import Iterable, List


def find_incresing(seq: Iterable[int]):
    return len([n for i, n in enumerate(seq[1:]) if n > seq[i]])


def parse_input(puzzle_input: str) -> List[int]:
    return [int(n) for n in puzzle_input.splitlines() if n != ""]


def solution_1(puzzle_input: str):
    return find_incresing(parse_input(puzzle_input))


def solution_2(puzzle_input: str):
    deeps = parse_input(puzzle_input)
    deep_sums = [n + deeps[i + 1] + deeps[i + 2] for i, n in enumerate(deeps[:-2])]
    return find_incresing(deep_sums)
drop-shadow(1px 0 0px #fff) drop-shadow(0 1px 0 #fff) drop-shadow(-1px 0 0 #fff) drop-shadow(0 -1px 0 #fff);
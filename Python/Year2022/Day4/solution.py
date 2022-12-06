import re


def parse_data(puzzle_input: str) -> list[list[int]]:
    pattern = r"(\d+)-(\d+),(\d+)-(\d+)"
    return [[int(v) for v in line] for line in re.findall(pattern, puzzle_input)]


def does_contain_another(e1_s: int, e1_e: int, e2_s: int, e2_e: int) -> bool:
    e1_c_e2 = e1_s <= e2_s and e1_e >= e2_e
    e2_c_e1 = e2_s <= e1_s and e2_e >= e1_e
    return e1_c_e2 or e2_c_e1


def is_overlaping(e1_s: int, e1_e: int, e2_s: int, e2_e: int) -> bool:
    e1 = {n for n in range(e1_s, e1_e + 1)}
    e2 = {n for n in range(e2_s, e2_e + 1)}
    return len(e1.intersection(e2)) > 0


def solution_1(puzzle_input: str) -> int:
    data = parse_data(puzzle_input)
    return sum([does_contain_another(*pair) for pair in data])


def solution_2(puzzle_input: str) -> int:
    data = parse_data(puzzle_input)
    return sum([is_overlaping(*pair) for pair in data])

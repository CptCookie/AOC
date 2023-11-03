from itertools import count


def parse_input(aoc_input: str) -> list[int]:
    return [int(n) for n in aoc_input.splitlines() if n != ""]


def solution_1(aoc_input: str):
    dfs = parse_input(aoc_input)
    return sum(dfs)


def solution_2(aoc_input: str):
    dfs = parse_input(aoc_input)
    cf = 0
    known_f = set()
    for ptr in count():
        cf += dfs[ptr % len(dfs)]

        if cf in known_f:
            return cf

        known_f.add(cf)

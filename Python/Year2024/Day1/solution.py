from collections import defaultdict


def parse_input(aoc_input: str) -> tuple[list[int], list[int]]:
    lines = (map(int, n.split("   ")) for n in aoc_input.splitlines())
    left, right = zip(*lines)
    return list(left), list(right)


def solution_1(aoc_input: str):
    left, right = map(sorted, parse_input(aoc_input))
    return sum(abs(right[i] - l) for i, l in enumerate(left))


def solution_2(aoc_input: str):
    left, right = parse_input(aoc_input)
    elem_count = defaultdict(int)
    for e in right:
        elem_count[e] += 1
    return sum(elem_count[l] * l for l in left)

import re

MAX = 4294967295


def parse_input(aoc_input: str):
    input = []
    for m in re.finditer(r"(\d+)-(\d+)", aoc_input):
        a, b = m.groups()
        input.append((int(a), int(b)))
    return input


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    input.sort(key=lambda x: x[0])
    highest = 0
    for f, t in input:
        if highest < f - 1:
            return highest + 1
        highest = max(highest, t)

    return highest


def solution_2(aoc_input: str, max_num=MAX):
    input = parse_input(aoc_input)
    input.sort(key=lambda x: x[0])
    allowed = 0
    highest_block = 0
    for f, t in input:
        if highest_block < f - 1:
            allowed += f - (highest_block + 1)
        highest_block = max(highest_block, t)

    allowed += max_num - highest_block

    return allowed

import re
from collections import Counter


def parse_patterns(puzzle_input):
    return {
        key: value for key, value in re.findall(r"([A-Z]{2}) -> ([A-Z])", puzzle_input)
    }


def count_for_cicle(polymer, patterns, cicle):
    elements = Counter(polymer)
    parts = Counter([polymer[i] + polymer[i + 1] for i in range(len(polymer) - 1)])

    for _ in range(cicle):
        parts, old_parts = Counter(), parts

        for (a, b), add in patterns.items():
            parts[a + add] += old_parts[a + b]
            parts[add + b] += old_parts[a + b]
            elements[add] += old_parts[a + b]
    return elements


def solution_1(puzzle_input: str):
    polymer = puzzle_input.splitlines()[0]
    patterns = parse_patterns(puzzle_input)
    elem_count = count_for_cicle(polymer, patterns, 10)
    return elem_count.most_common()[0][1] - elem_count.most_common()[-1][1]


def solution_2(puzzle_input: str):
    polymer = puzzle_input.splitlines()[0]
    patterns = parse_patterns(puzzle_input)
    elem_count = count_for_cicle(polymer, patterns, 40)
    return elem_count.most_common()[0][1] - elem_count.most_common()[-1][1]

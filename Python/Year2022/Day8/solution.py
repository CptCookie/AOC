from operator import mul
from functools import reduce


def parse_data(puzzle_input: str) -> list[str]:
    return [
        [int(tree) for tree in line] for line in puzzle_input.splitlines() if line != ""
    ]


def get_sightlines(trees: list[list[int]], pos: tuple[int, int]) -> list[list[int]]:
    x, y = pos
    sightlines = []
    sightlines.append(list(reversed(trees[y][:x])))  # left
    sightlines.append(trees[y][x + 1 :])  # right

    # up
    sightlines.append(list(reversed([t[x] for i, t in enumerate(trees) if i < y])))
    sightlines.append([t[x] for i, t in enumerate(trees) if i > y])  # down
    return sightlines


def is_tree_visible(tree: int, sightlines: list[list[int]]) -> bool:
    for line in sightlines:
        if len(line) == 0:
            return True

        if all([t < tree for t in line]):
            return True

    return False


def get_sceenic_value(tree: int, sightlines: list[list[int]]) -> int:
    values = []
    for line in sightlines:
        if len(line) == 0:
            values.append(0)

        for i, t in enumerate(line):
            if t >= tree:
                values.append(i + 1)
                break

            if i == len(line) - 1:
                values.append(i + 1)

    return reduce(mul, values)


def solution_1(puzzle_input: str):
    trees = parse_data(puzzle_input)
    count = 0
    for y, line in enumerate(trees):
        for x, t in enumerate(line):
            if is_tree_visible(t, get_sightlines(trees, (x, y))):
                count += 1
    return count


def solution_2(puzzle_input: str):
    trees = parse_data(puzzle_input)
    sceen = 0
    for y, line in enumerate(trees):
        for x, t in enumerate(line):
            value = get_sceenic_value(t, get_sightlines(trees, (x, y)))
            sceen = max(sceen, value)
    return sceen

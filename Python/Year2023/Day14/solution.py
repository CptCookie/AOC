from copy import deepcopy
from typing import TypeAlias

Pos: TypeAlias = tuple[int, int]

ROUND_ROCK = "O"
FREE = "."

NORTH = (0, -1)
EAST = (1, 0)
SOUTH = (0, 1)
WEST = (-1, 0)


def parse_rocks(aoc_input: str) -> tuple[set[Pos], set[Pos]]:
    loose, fixed = set(), set()

    for y, line in enumerate(aoc_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case "O":
                    loose.add((x, y))
                case "#":
                    fixed.add((x, y))

    # add fixed rocks outside the dish to enclose it
    for n in range(-1, x + 2):
        fixed.add((n, y + 1))
        fixed.add((n, -1))

    for n in range(-1, y + 2):
        fixed.add((x + 1, n))
        fixed.add((-1, n))

    return fixed, loose


def get_direction_sort(rocks: set[Pos], direction) -> list[Pos]:
    return sorted(
        rocks, key=lambda p: p[0] * direction[0] * -1 + p[1] * direction[1] * -1
    )


def tilt_dish(fixed: set[Pos], loose: set[Pos], direction: Pos) -> set[Pos]:
    dx, dy = direction
    settled = False

    while not settled:
        settled = True
        new_loose = set()
        for x, y in get_direction_sort(loose, direction):
            npos = (x + dx, y + dy)
            if npos not in new_loose and npos not in fixed:
                new_loose.add((x + dx, y + dy))
                settled = False
            else:
                new_loose.add((x, y))
        loose = new_loose

    return loose


def calc_load_rocks(fixed, loose):
    max_pos = max(fixed, key=lambda p: p[1])
    return sum((max_pos[1] - y) for x, y in loose)


def solution_1(aoc_input: str):
    fixed, loose = parse_rocks(aoc_input)
    loose = tilt_dish(fixed, loose, NORTH)
    return calc_load_rocks(fixed, loose)


def solution_2(aoc_input: str):
    fixed, loose = parse_rocks(aoc_input)
    known = [deepcopy(loose)]
    for n in range(1000000000):
        for d in [NORTH, WEST, SOUTH, EAST]:
            loose = tilt_dish(fixed, loose, d)

        if loose in known:
            idx = known.index(loose)
            seq_len = len(known) - idx
            remain = (1000000000 - n - 1) % seq_len
            return calc_load_rocks(fixed, known[idx + remain])
        else:
            known.append(deepcopy(loose))

    return calc_load_rocks(fixed, loose)

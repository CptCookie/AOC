import heapq
import re
from collections import deque
from typing import Iterable

Coord2D = tuple[int, int]
INPUT_PATTERN = r"([UDLR]) (\d+) \(#([\da-f]+)\)"
DIRECTIONS = {
    "U": (0, -1),
    "D": (0, 1),
    "R": (1, 0),
    "L": (-1, 0),
}


def parse_input(aoc_input: str) -> list[tuple[str, int, str]]:
    instructions = []
    for m in re.finditer(INPUT_PATTERN, aoc_input):
        direction, distance, color = m.groups()
        instructions.append((direction, int(distance), color))
    return instructions


def dig_trench(instructions: list[tuple[str, int, str]]) -> set[Coord2D]:
    trench = []

    x, y = 0, 0
    for d, dist, _ in instructions:
        dx, dy = DIRECTIONS[d]
        trench.extend([(x + dx * i, y + dy * i) for i in range(1, dist + 1)])
        x, y = x + dx * dist, y + dy * dist
    return set(trench)


def dig_inside(trench: set[Coord2D], direct: str) -> set[Coord2D]:
    fill_pos = get_fill_pos(direct)
    for fill in fill_pos:
        try:
            dug: set[Coord2D] = dig_inside_from_pos(trench, fill)
            return trench.union(dug)
        except IndexError:
            pass

    raise ValueError("Can not dir inside the trench")


def dig_inside_from_pos(trench: set[Coord2D], fill: Coord2D) -> set[Coord2D]:
    min_x, max_x = min(x for (x, _) in trench), max(x for (x, _) in trench)
    min_y, max_y = min(y for (_, y) in trench), max(y for (_, y) in trench)

    q = deque([fill])
    dug = set()

    while q:
        x, y = q.popleft()

        if min_x > x or x > max_x or min_y > y or y > max_y:
            raise IndexError

        if (x, y) not in dug:
            dug.add((x, y))

            for dx, dy in DIRECTIONS.values():
                if (x + dx, y + dy) not in trench and (x + dx, y + dy) not in dug:
                    q.append((x + dx, y + dy))
    return dug


def get_fill_pos(direct: str) -> list[Coord2D]:
    x, y = DIRECTIONS[direct]

    if direct in ("R", "L"):
        return [(x, y - 1), (x, y + 1)]
    else:
        return [(x + 1, y), (x, y)]


def print_lagoon(dig: Iterable[Coord2D]):
    min_x, max_x = min(x for (x, _) in dig), max(x for (x, _) in dig)
    min_y, max_y = min(y for (_, y) in dig), max(y for (_, y) in dig)

    print(min_x, max_x, min_y, max_y)

    for y in range(0, max_y - min_y + 1):
        for x in range(0, max_x - min_x + 1):
            if (x + min_x, y + min_y) in dig:
                print("#", end="")
            else:
                print(".", end="")

        print()


TEST_INPUT = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""


def solution_1(aoc_input: str):
    instr = parse_input(aoc_input)
    trench = dig_trench(instr)
    lagoon = dig_inside(trench, instr[0][0])
    print_lagoon(lagoon)
    return len(lagoon)


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return None

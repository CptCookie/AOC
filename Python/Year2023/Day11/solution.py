from typing import TypeAlias

Map: TypeAlias = list[str]
Pos: TypeAlias = tuple[int, int]

EMPTY = "."
GALAXY = "#"


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def get_galaxie_pos(universe: Map) -> list[Pos]:
    return [
        (x, y)
        for y, line in enumerate(universe)
        for x, c in enumerate(line)
        if c == GALAXY
    ]


def get_empty_rows(universe: Map) -> set[int]:
    return set(i for i, line in enumerate(universe) if all(c == EMPTY for c in line))


def get_empty_cols(universe: Map) -> set[int]:
    empty = set()

    for x in range(len(universe[0])):
        col = [line[x] for line in universe]
        if all(c == EMPTY for c in col):
            empty.add(x)

    return empty


def distance(
    a: Pos,
    b: Pos,
    empty_col: set[int],
    empty_row: set[int],
    expansion: int,
) -> int:
    # base distance
    d = abs(a[0] - b[0]) + abs(a[1] - abs(b[1]))

    # add expansion by empty columns
    for c in empty_col:
        if min(a[0], b[0]) < c < max(a[0], b[0]):
            d += expansion - 1

    # add expansion by empty rows
    for r in empty_row:
        if min(a[1], b[1]) < r < max(a[1], b[1]):
            d += expansion - 1

    return d


def solution_1(aoc_input: str):
    universe = parse_input(aoc_input)
    galaxies = get_galaxie_pos(universe)
    empty_col = get_empty_cols(universe)
    empty_row = get_empty_rows(universe)

    sum_dist = 0
    for i, a in enumerate(galaxies):
        for b in galaxies[i:]:
            sum_dist += distance(a, b, empty_col, empty_row, 2)
    return sum_dist


def solution_2(aoc_input: str, expansion=1_000_000):
    universe = parse_input(aoc_input)
    galaxies = get_galaxie_pos(universe)
    empty_col = get_empty_cols(universe)
    empty_row = get_empty_rows(universe)

    sum_dist = 0
    for i, a in enumerate(galaxies):
        for b in galaxies[i:]:
            sum_dist += distance(a, b, empty_col, empty_row, expansion)
    return sum_dist

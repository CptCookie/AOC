from typing import TypeAlias

Pos: TypeAlias = tuple[int, int]
Map: TypeAlias = list[str]

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]


def parse_input(aoc_input: str) -> (Pos, Map):
    pos = None
    map = [n for n in aoc_input.splitlines() if n != ""]

    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == "^":
                pos = (x, y)
                map[y] = map[y].replace("^", ".")

    return pos, map


def get_visited(start: Pos, map: Map):
    visited: set[Pos] = {start}
    x, y = start
    dir_idx = 0  # idx of DIRECTIONS
    while True:
        dx, dy = DIRECTIONS[dir_idx]
        nx, ny = x + dx, y + dy

        if not 0 <= ny < len(map) or not 0 <= nx < len(map[0]):
            return visited
        if map[y + dy][x + dx] == "#":
            dir_idx = (dir_idx + 1) % len(DIRECTIONS)
        else:
            x, y = x + dx, y + dy
            visited.add((x, y))


def is_looping(start: Pos, obstruction: Pos, map: Map):
    x, y = start
    dir_idx = 0  # idx of DIRECTIONS
    turns: set[Pos] = set()

    while True:
        dx, dy = DIRECTIONS[dir_idx]
        nx, ny = x + dx, y + dy

        if not 0 <= ny < len(map) or not 0 <= nx < len(map[-1]):
            # leaved the map
            return False

        if map[ny][nx] == "#" or (nx, ny) == obstruction:
            # obstruction
            if (x, y) in turns:
                # we did already turn here -> loop detected
                return True
            while map[ny][nx] == "#" or (nx, ny) == obstruction:
                # turn until path is free and set new position
                dir_idx = (dir_idx + 1) % len(DIRECTIONS)
                dx, dy = DIRECTIONS[dir_idx]
                nx, ny = x + dx, y + dy
            turns.add((x, y))

        x, y = nx, ny


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return len(get_visited(*input))


def solution_2(aoc_input: str) -> int:
    start, map = parse_input(aoc_input)
    visited = get_visited(start, map)
    counter = 0
    for pos in visited - {start}:
        if is_looping(start, pos, map):
            counter += 1

    return counter

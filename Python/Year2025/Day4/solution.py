Position = tuple[int, int]
Map = list[list[str]]

PAPER = "@"
EMPTY = "."

NEIGHBORS = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)


def parse_input(aoc_input: str) -> Map:
    return [list(n) for n in aoc_input.splitlines() if n != ""]


def get_adjacent_papers(storage_map: Map, pos: Position) -> list[Position]:
    x, y = pos
    adj = []

    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(storage_map[0]) and 0 <= ny < len(storage_map):
            adj.append((nx, ny))

    return [(x, y) for (x, y) in adj if storage_map[y][x] == PAPER]


def get_movable(storage_map: Map):
    movable = []
    for y, line in enumerate(storage_map):
        for x, c in enumerate(line):
            adjacent_paper = get_adjacent_papers(storage_map, (x, y))
            if c == PAPER and len(adjacent_paper) < 4:
                movable.append((x, y))

    return movable


def remove_rolls(storage_map: Map) -> int:
    remove_cnt = 0
    while movable := get_movable(storage_map):
        for x, y in movable:
            remove_cnt += 1
            storage_map[y][x] = EMPTY

    return remove_cnt


def solution_1(aoc_input: str):
    storage_map = parse_input(aoc_input)
    return len(get_movable(storage_map))


def solution_2(aoc_input: str):
    storage_map = parse_input(aoc_input)
    return remove_rolls(storage_map)

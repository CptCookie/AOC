Position = tuple[int, int]


NEIGHBORS = (
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (0, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
)


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def get_adjacent(paper_map: list[str], pos: Position) -> list[Position]:
    x, y = pos
    adj = []
    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy

        if 0 <= nx <= len(paper_map[0]) and 0 <= ny <= len(paper_map):
            adj.append(adj)

    return adj


def get_movable(paper_map: list[str]):
    movable = []
    for y, line in enumerate(paper_map):
        for x, c in enumerate(line):
            if c == "@" and len(get_adjacent(paper_map, (x, y))) < 4:
                movable.append((x, y))

    return movable


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return len(get_movable(input))


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return None

Position = tuple[int, int]
Map = list[list[str]]

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


def get_adjacent_papers(paper_map: Map, pos: Position) -> list[Position]:
    x, y = pos
    adj = []

    for dx, dy in NEIGHBORS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(paper_map[0]) and 0 <= ny < len(paper_map):
            adj.append((nx, ny))

    return [(x, y) for (x, y) in adj if paper_map[y][x] == "@"]


def get_movable(paper_map: Map):
    movable = []
    for y, line in enumerate(paper_map):
        for x, c in enumerate(line):
            adjacent_paper = get_adjacent_papers(paper_map, (x, y))
            if c == "@" and len(adjacent_paper) < 4:
                movable.append((x, y))

    return movable


def remove_rolls(paper_map: Map) -> int:
    remove_cnt = 0
    while movable := get_movable(paper_map):
        for x, y in movable:
            remove_cnt += 1
            paper_map[y][x] = "."

    return remove_cnt


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return len(get_movable(input))


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return remove_rolls(input)

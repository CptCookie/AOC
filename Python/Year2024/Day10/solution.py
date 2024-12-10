from collections import deque

TopoMap = tuple[tuple[int, ...], ...]
Pos = tuple[int, int]

NEIGHBORS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def parse_input(aoc_input: str) -> TopoMap:
    return tuple(tuple(map(int, n)) for n in aoc_input.splitlines() if n != "")


def get_start_positions(map: TopoMap) -> list[Pos]:
    starts = []

    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c == 0:
                starts.append((x, y))

    return starts


def get_trailhead_score(head: Pos, map: TopoMap) -> int:
    height, width = len(map[0]), len(map)
    q = deque()
    q.append(head)
    finishes = set()

    while q:
        x, y = q.popleft()
        value = map[y][x]

        if value == 9:
            finishes.add((x, y))
            continue

        for dx, dy in NEIGHBORS:
            nx, ny = x + dx, y + dy
            in_map = 0 <= nx < width and 0 <= ny < height

            if in_map and map[y + dy][x + dx] - value == 1:
                q.append((x + dx, y + dy))
    return len(finishes)


def get_trailhead_rating(head: Pos, map: TopoMap) -> int:
    height, width = len(map[0]), len(map)
    q = deque()
    q.append(head)
    rating = 0

    while q:
        x, y = q.popleft()
        value = map[y][x]

        if value == 9:
            rating += 1
            continue

        for dx, dy in NEIGHBORS:
            nx, ny = x + dx, y + dy
            in_map = 0 <= nx < width and 0 <= ny < height

            if in_map and map[y + dy][x + dx] - value == 1:
                q.append((x + dx, y + dy))
    return rating


def calculate_total_score(map: TopoMap) -> int:
    return sum(get_trailhead_score(head, map) for head in get_start_positions(map))


def calculate_total_rating(map: TopoMap) -> int:
    return sum(get_trailhead_rating(head, map) for head in get_start_positions(map))


def solution_1(aoc_input: str):
    map = parse_input(aoc_input)
    return calculate_total_score(map)


def solution_2(aoc_input: str):
    map = parse_input(aoc_input)
    return calculate_total_rating(map)

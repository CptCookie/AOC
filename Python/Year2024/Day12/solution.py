from collections import deque

Map = tuple[str, ...]
Pos = tuple[int, int]

NEIGHBORS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
CORNER = [(1, 1), (-1, 1), (-1, -1), (1, -1)]


def parse_input(aoc_input: str) -> Map:
    return tuple(n for n in aoc_input.splitlines() if n != "")


def get_connected_plot_fields(start: Pos, map: Map) -> set[Pos]:
    width, height = len(map[0]), len(map)
    q = deque()
    q.append(start)
    connected = {start}
    plant = map[start[1]][start[0]]

    while q:
        x, y = q.popleft()

        for dx, dy in NEIGHBORS:
            nx, ny = x + dx, y + dy
            in_map = 0 <= nx < width and 0 <= ny < height
            visited = (nx, ny) in connected

            if in_map and not visited and map[ny][nx] == plant:
                q.append((nx, ny))
                connected.add((nx, ny))

    return connected


def get_all_plots(map: Map) -> list[set[Pos]]:
    plots = []
    allocated_fields = set()

    for y, line in enumerate(map):
        for x, field in enumerate(line):
            if (x, y) in allocated_fields:
                continue

            plot = get_connected_plot_fields((x, y), map)
            plots.append(plot)
            allocated_fields |= plot

    return plots


def get_number_faces(plots: set[Pos]) -> int:
    faces = 0
    for p in plots:
        faces += count_corners(p, plots)

    return faces


def count_corners(pos, plots):
    x, y = pos
    corner_count = 0
    for dx, dy in CORNER:
        corner = (x + dx, y + dy)
        adjacent_1 = (x + dx, y)
        adjacent_2 = (x, y + dy)

        # inner corner
        corner_count += (
            corner not in plots and adjacent_1 in plots and adjacent_2 in plots
        )

        # outer corner
        corner_count += (
            corner not in plots and adjacent_1 not in plots and adjacent_2 not in plots
        )

        # diagonal corner on corner
        corner_count += (
            corner in plots and adjacent_1 not in plots and adjacent_2 not in plots
        )

    return corner_count


def get_plot_price_by_faces(plot: set[Pos], map: Map) -> int:
    x, y = plot.__iter__().__next__()
    faces = get_number_faces(plot)
    price = faces * len(plot)

    return price


def get_plot_price_by_fence(plot: set[Pos]) -> int:
    fence = 0
    for x, y in plot:
        neighbors = len([1 for dx, dy in NEIGHBORS if (x + dx, y + dy) in plot])
        fence += 4 - neighbors
    return fence * len(plot)


def solution_1(aoc_input: str):
    map = parse_input(aoc_input)
    plots = get_all_plots(map)
    return sum(get_plot_price_by_fence(p) for p in plots)


def solution_2(aoc_input: str):
    map = parse_input(aoc_input)
    plots = get_all_plots(map)
    return sum(get_plot_price_by_faces(p, map) for p in plots)

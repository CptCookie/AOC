from copy import deepcopy


def parse_points(aoc_input):
    points = []
    for line in aoc_input.strip().split("\n"):
        x, y = line.split(", ")
        points.append((int(x), int(y)))

    return points


def max_point(points: [(int, int)]):
    return max(n for p in points for n in p)


def area_all_occupation(points: [(int, int)], max_dist=10000):
    max_p = max_point(points)
    area = 0

    for y in range(max_p + 1):
        for x in range(max_p + 1):
            if sum(abs(x-px) + abs(y-py) for px, py in points) < max_dist:
                area += 1

    return area

def grid_single_occupation(points: [(int, int)]):
    max_p = max_point(points)
    grid = [[[] for _ in range(max_p + 1)] for _ in range(max_p + 1)]
    stable = False
    dist = 0

    while not stable:
        stable = True
        next_grid = deepcopy(grid)

        for p in points:
            for nx, ny in get_distant_coord(p, dist):
                if 0 <= ny <= max_p and 0 <= nx <= max_p:
                    if grid[ny][nx] == []:
                        next_grid[ny][nx].append(p)
                        stable = False
        grid = next_grid
        dist += 1

    # filter  points that are occupied more than once
    for y, line in enumerate(grid):
        for x, values in enumerate(line):
            if len(values) > 1:
                grid[y][x] = []
    return grid


def get_biggest_single_area(grid):
    infinite_points = grid[0] + grid[-1] + [grid[n][0] for n in range(len(grid))] +  [grid[n][-1] for n in range(len(grid))]
    infinite_points = set(n for v in infinite_points for n in v if v != [])
    for y, line in enumerate(grid):
        for x, values in enumerate(line):
            if values != [] and values[0] in infinite_points:
                grid[y][x] = []


    elements = [v[0] for y in grid for v in y if v != []]
    return max(elements.count(v) for v in set(elements))


def get_distant_coord(point: (int, int), dist: int):
    x, y = point
    if dist == 0:
        return [point]

    dist_points = (
        [(x + i, y + dist - i) for i in range(dist)]  # top right
        + [(x + dist - i, y - i) for i in range(dist)]  # bottom right
        + [(x - i, y - dist + i) for i in range(dist)]  # bottom left
        + [(x - dist + i, y + i) for i in range(dist)]  # top left
    )

    return dist_points


def solution_1(aoc_input: str):
    grid = grid_single_occupation(parse_points(aoc_input))
    return get_biggest_single_area(grid)


def solution_2(aoc_input: str):
     return area_all_occupation(parse_points(aoc_input))

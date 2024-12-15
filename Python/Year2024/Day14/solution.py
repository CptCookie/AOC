import re
from statistics import stdev, mean

Guard = tuple[int, int, int, int]


def parse_input(aoc_input: str) -> list[Guard]:
    pattern = re.compile(r"p=([-\d]+),([-\d]+) v=([-\d]+),([-\d]+)")
    return [tuple(map(int, m.groups())) for m in pattern.finditer(aoc_input)]


def calculate_pos(guard: Guard, width: int, height: int, t: int) -> tuple[int, int]:
    x, y, dx, dy = guard

    return (x + dx * t) % width, (y + dy * t) % height


def safety_ratings(guards: list[Guard], width: int, height: int, t: int) -> int:
    guard_pos = [calculate_pos(g, width, height, t) for g in guards]

    limit_x, limit_y = (width - 1) / 2, (height - 1) / 2

    tl = sum([1 for x, y in guard_pos if x < limit_x and y < limit_y])
    tr = sum([1 for x, y in guard_pos if x > limit_x and y < limit_y])
    bl = sum([1 for x, y in guard_pos if x < limit_x and y > limit_y])
    br = sum([1 for x, y in guard_pos if x > limit_x and y > limit_y])
    print(tl, tr, bl, br)
    return tl * tr * bl * br


def print_map(guards: list[tuple[int, int]], width: int, height: int) -> None:
    print("\nGuards:")
    for y in range(height):
        for x in range(width):
            count = guards.count((x, y))
            if count > 0:
                print("\u2588", end=" ")
            else:
                print("\u2007", end=" ")
        print("")


def get_christmas_tree(guards: list[Guard], width: int, height: int) -> int:
    t = 1
    dt = 1
    deviations = []

    while True:
        guard_x, guard_y = [], []
        for guard in guards:
            x, y = calculate_pos(guard, width, height, t)
            guard_x.append(x)
            guard_y.append(y)

        if dt == 1:
            cluster_value = stdev(guard_x)
        else:
            cluster_value = stdev(guard_y)

        deviations.append(cluster_value)
        mean_cluster = mean(deviations)

        if cluster_value < mean_cluster * 0.8 and dt == 1:
            deviations = [stdev(guard_y)]
            dt = width
        elif cluster_value < mean_cluster * 0.8 and dt == width:
            return t
        elif t > 10000:
            raise Exception("no cluster")

        t += dt


def solution_1(aoc_input: str):
    guards = parse_input(aoc_input)
    return safety_ratings(guards, 101, 103, 100)


def solution_2(aoc_input: str):
    guards = parse_input(aoc_input)
    return get_christmas_tree(guards, 101, 103)

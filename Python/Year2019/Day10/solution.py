import math


def parse_input(aoc_input: str) -> list[tuple[int, int]]:
    asteriods = []
    for y, line in enumerate(aoc_input.split("\n")):
        for x, c in enumerate(line):
            if c == "#":
                asteriods.append((x, y))
    return asteriods


def get_num_visible(asteriods: list[tuple[int, int]], station: tuple[int, int]) -> int:
    directions = set()
    sx, sy = station
    for ax, ay in asteriods:
        if (ax, ay) != station:
            dx, dy = ax - sx, ay - sy
            ld = abs(dx) + abs(dy)
            norm_dx, norm_dy = dx / ld, dy / ld
            directions.add((norm_dx, norm_dy))

    return len(directions)


def astroid_rad_north_normal(center, orbit):
    cx, cy = center
    ox, oy = orbit

    dx, dy = ox - cx, oy - cy

    if dx >= 0 and dy < 0:
        return math.atan(dx / abs(dy))

    if dx > 0 and dy >= 0:
        return 1 / 2 * math.pi + math.atan(dy / dx)

    if dx <= 0 and dy > 0:
        return math.pi + math.atan(abs(dx) / dy)

    if dx < 0 and dy <= 0:
        return 3 / 2 * math.pi + math.atan(abs(dy) / abs(dx))


def get_first_vaporized(asteriods: [(int, int)], station: (int, int)) -> (int, int):
    directions = set()
    asteriods_rad = {}
    sx, sy = station

    for ax, ay in asteriods:
        if (ax, ay) == station:
            continue

        rad = astroid_rad_north_normal(station, (ax, ay))
        if rad in asteriods_rad:
            # in that direction already found check which is closer
            ox, oy = asteriods_rad[rad]
            if abs(sx - ox) + abs(sy - oy) > abs(sx - ax) + abs(sy - ay):
                asteriods_rad[rad] = (ax, ay)
        else:
            # no astoroid in that direction known
            asteriods_rad[rad] = (ax, ay)

    return [asteriods_rad[rad] for rad in sorted(list(asteriods_rad.keys()))]


def solution_1(aoc_input: str):
    asteriods = parse_input(aoc_input)
    return max(get_num_visible(asteriods, a) for a in asteriods)


def solution_2(aoc_input: str):
    asteriods = parse_input(aoc_input)
    visible = [(a, get_num_visible(asteriods, a)) for a in asteriods]
    station, v = max(visible, key=lambda x: x[1])
    assert v == 309
    vaporized = get_first_vaporized(asteriods, station)
    vx, vy = vaporized[199]
    return vx * 100 + vy

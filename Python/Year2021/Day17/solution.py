import math, re
from operator import add


def calc_pos(init_vel, step):
    return ((1 + 2 * init_vel) * step - step ** 2) / 2


def dimension_passes_area(init_vel, pos_1, pos_2):
    z = 1 + 2 * init_vel

    try:
        s1 = z / 2 + math.sqrt(z ** 2 / 4 - 2 * max(pos_1, pos_2))
        s2 = z / 2 + math.sqrt(z ** 2 / 4 - 2 * min(pos_1, pos_2))

        if max(s1, s2) // 1 - min(s1, s2) // 1 >= 1.0:
            return [
                n
                for n in range(int(min(s1, s2)), int(max(s1, s2)) + 1)
                if min(s1, s2) <= n <= max(s1, s2)
            ]

    except ValueError:
        pass

    return []


def passes_area_xy(init_velos, area_x, area_y):
    # calculate steps with y coordiantes
    y_hits = dimension_passes_area(init_velos[1], *area_y)
    return y_hits and any(
        [min(area_x) < calc_pos(init_velos[0], n) < max(area_x) for n in y_hits]
    )


def iterate_throw(velos, area_x, area_y):
    vel = [n for n in velos]
    pos = [0, 0]
    while True:
        pos = [add(*n) for n in zip(pos, vel)]

        if min(area_x) <= pos[0] <= max(area_x) and min(area_y) <= pos[1] <= max(
            area_y
        ):
            return True
        if max(area_x) <= pos[0] or min(area_y) > pos[1] and vel[1] < 0:
            return False

        vel[1] -= 1
        if abs(vel[0]) > 0:
            vel[0] = (abs(vel[0]) - 1) * vel[0] // abs(vel[0])


def parse_data(puzzle_input: str) -> list[str]:

    return (
        int(n)
        for n in re.search(
            r"target area: x=(\d+)..(\d+), y=(\-\d+)..(\-\d+)", puzzle_input
        ).groups()
    )


def solution_1(puzzle_input: str):
    _, _, y1, y2 = parse_data(puzzle_input)
    max_vel = [i for i in range(1000) if dimension_passes_area(i, y1, y2)]
    return calc_pos(max_vel[-1], max_vel[-1])


def solution_2(puzzle_input: str):
    x1, x2, y1, y2 = parse_data(puzzle_input)

    hits = [
        1
        for y in range(min(y1, y1) - 1, abs(max(y1, y1)) + 1)
        for x in range(max(x1, x2) + 1)
        if iterate_throw([x, y], area_x=[x1, x2], area_y=[y1, y2])
    ]

    return len(hits)

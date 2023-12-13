from typing import TypeAlias

Reading: TypeAlias = list[int]


def parse_input(aoc_input: str) -> list[Reading]:
    readings = []

    for line in aoc_input.splitlines():
        readings.append([int(n) for n in line.split(" ")])

    return readings


def build_diff_triangle(reading: Reading) -> list[Reading]:
    triangle = [reading]

    while len(set(triangle[-1])) > 1:
        triangle.append([x - triangle[-1][i] for i, x in enumerate(triangle[-1][1:])])

    return triangle


def extrapolate_next_value(reading: Reading) -> int:
    triangle = build_diff_triangle(reading)

    for i, line in enumerate(reversed(triangle)):
        if i == 0:
            line.append(line[0])
        else:
            line.append(
                triangle[len(triangle) - i - 1][-1] + triangle[len(triangle) - i][-1]
            )

    return triangle[0][-1]


def extrapolate_prev_value(reading: Reading) -> int:
    triangle = build_diff_triangle(reading)

    for i, line in enumerate(reversed(triangle)):
        if i == 0:
            line.append(line[0])
        else:
            idx = len(triangle) - i - 1
            value = triangle[idx][0] - triangle[idx + 1][0]
            triangle[idx] = [value] + triangle[idx]

    return triangle[0][0]


def solution_1(aoc_input: str) -> int:
    readings = parse_input(aoc_input)
    return sum(extrapolate_next_value(r) for r in readings)


def solution_2(aoc_input: str) -> int:
    readings = parse_input(aoc_input)
    return sum(extrapolate_prev_value(r) for r in readings)

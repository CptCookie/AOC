import re


def parse_input(puzzle_input: str) -> list[str]:
    pattern = r".+ at x=(-?\d+), y=(-?\d+).+x=(-?\d+), y=(-?\d+)"
    return [[int(i) for i in n] for n in re.findall(pattern, puzzle_input) if n != ""]


def get_covered_line(input, line):
    coverage = []
    for s in input:
        coverage.extend(get_sensor_line(s, line))

    for b in input:
        if b[2] in coverage and b[3] == line:
            coverage.remove(b[2])
    return set(coverage)


def get_sensor_line(input, line):
    xs, ys, xb, yb = input
    distance = abs(xs - xb) + abs(ys - yb)

    if ys + distance + 1 >= line >= ys - distance - 1:
        width = (distance - abs(line - ys)) * 2 + 1
        return [xs + d for d in range(-(width // 2), width // 2 + 1)]
    else:
        return []


def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    return len(get_covered_line(input, 2000000))


def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    for _, _, x, y in input:
        if x < 4000000 and y < 4000000 and x > 0 and y > 0:
            return x * 4000000 + y

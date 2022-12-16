import re


def parse_input(puzzle_input: str) -> list[list[int]]:
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


def get_sensor_range(input):
    sensor_ranges = [(xs, ys, abs(xs - xb) + abs(ys - yb)) for xs, ys, xb, yb in input]
    return sensor_ranges


def get_sensor_line_ranges(x, y, dist, layer) -> tuple[int, int]:
    if y + dist + 1 >= layer >= y - dist - 1:
        return x - (dist - abs(y - layer)), x + (dist - abs(y - layer))


def get_sensor_fring(x, y, sensor_range):
    fringe_pnts = []
    for layer in range(y - sensor_range - 1, y + sensor_range + 2):
        if layer == y - sensor_range - 1 or layer == y + sensor_range + 1:
            fringe_pnts.append((x, layer))
        else:
            sensor_layer_range = get_sensor_line_ranges(x, y, sensor_range, layer)
            fringe_pnts.append((sensor_layer_range[0] - 1, layer))
            fringe_pnts.append((sensor_layer_range[1] + 1, layer))
    return fringe_pnts


def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    return len(get_covered_line(input, 2000000))


def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    srange = get_sensor_range(input)
    fringes = []
    for s in srange:
        fringes.extend(get_sensor_fring(*s))

    for xf, yf in fringes:
        if 0 <= xf <= 4_000_000 and  0 <= yf <= 4_000_000 :
            if all(abs(xf - xs) + abs(yf - ys) > dist for xs, ys, dist in srange ):
                return  xf*4_000_000 + yf



import re


def parse_data(puzzle_input: str):
    puzzle_data = []
    for line in puzzle_input.splitlines():
        if line != "":
            groups = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line).groups()
            puzzle_data.append(
                ((int(groups[0]), int(groups[1])), (int(groups[2]), int(groups[3])))
            )
    return puzzle_data


class HydroMap:
    def __init__(self, maxdimension):
        self.map = [[0] * maxdimension for _ in range(maxdimension)]

    def draw_line(self, start: tuple[int], end: tuple[int], diagonal=False):
        if start[0] == end[0] or start[1] == end[1]:
            x_range = sorted([start[0], end[0]])
            x_range[-1] += 1

            y_range = sorted([start[1], end[1]])
            y_range[-1] += 1

            for x in range(*x_range):
                for y in range(*y_range):
                    self.map[y][x] += 1
        elif diagonal:
            delta = abs(start[0] - end[0])
            x_rising = end[0] - start[0] > 0
            y_rising = end[1] - start[1] > 0

            for n in range(delta + 1):
                x = start[0] + n if x_rising else start[0] - n
                y = start[1] + n if y_rising else start[1] - n
                self.map[y][x] += 1


def solution_1(puzzle_input: str):
    puzzle_data = parse_data(puzzle_input)
    hydro_map = HydroMap(max([max(*start, *end) for start, end in puzzle_data]) + 1)
    for line in puzzle_data:
        hydro_map.draw_line(*line)

    return sum([cell > 1 for line in hydro_map.map for cell in line])


def solution_2(puzzle_input: str):
    puzzle_data = parse_data(puzzle_input)
    hydro_map = HydroMap(max([max(*start, *end) for start, end in puzzle_data]) + 1)
    for line in puzzle_data:
        hydro_map.draw_line(*line, diagonal=True)

    return sum([cell > 1 for line in hydro_map.map for cell in line])

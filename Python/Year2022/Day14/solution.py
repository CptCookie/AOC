from copy import deepcopy


AIR = "."
WALL = "#"
SAND = "o"


def parse_data(puzzle_input: str) -> list[str]:
    data = []
    for l in puzzle_input.splitlines():
        data_line = []
        for p in l.split("->"):
            data_line.append(tuple((int(v) for v in p.split(","))))
        data.append(data_line)
    return data


class Map:
    def __init__(self, walls, endless=True):
        xs = [p[0] for l in walls for p in l]
        ys = [p[1] for l in walls for p in l]

        if endless:
            self.max_y = max(ys)
            self.max_x = max(xs)
            self.min_x = min(xs)
        else:
            self.max_y = max(ys) + 2
            self.max_x = max(xs) + self.max_y + 1
            self.min_x = min(xs) - self.max_y - 1

        self.map = [
            [AIR for _ in range(self.max_x - self.min_x + 1)]
            for _ in range(self.max_y + 1)
        ]

        if not endless:
            for x in range(self.max_x - self.min_x + 1):
                self.map[self.max_y][x] = WALL

        self._built_map(walls)

    def _built_map(self, walls):
        for section in walls:
            for n, wall in enumerate(section[1:]):
                self._built_wall(section[n], wall)

    def _built_wall(self, from_pos, to_pos):
        from_x, from_y = from_pos
        to_x, to_y = to_pos

        if from_x != to_x and from_y == to_y:
            for x in range(min(from_x, to_x), max(from_x, to_x) + 1):
                self.map[to_y][x - self.min_x] = WALL
        elif from_y != to_y and from_x == to_x:
            for y in range(min(from_y, to_y), max(from_y, to_y) + 1):
                self.map[y][to_x - self.min_x] = WALL
        else:
            raise ValueError("Wall can not be diagonal")

    def pour_in_sand(self, source: tuple[int, int]):
        while True:
            try:
                self._palace_grain(source)
            except IndexError:
                return sum(1 for line in self.map for c in line if c == SAND)

    def _palace_grain(self, grain: tuple[int, int]):
        current_grain = deepcopy(grain)
        while True:
            gx, gy = current_grain
            if self.map[gy + 1][gx - self.min_x] == AIR:
                current_grain = (gx, gy + 1)
            elif self.map[gy + 1][gx - self.min_x - 1] == AIR:
                current_grain = (gx - 1, gy + 1)
            elif self.map[gy + 1][gx - self.min_x + 1] == AIR:
                current_grain = (gx + 1, gy + 1)
            elif (gx, gy) != grain:
                self.map[gy][gx - self.min_x] = SAND
                return
            else:
                raise IndexError("Grain could not move")


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    map = Map(data)
    return map.pour_in_sand((500, 0))


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    map = Map(data, endless=False)
    return map.pour_in_sand((500, 0)) + 1

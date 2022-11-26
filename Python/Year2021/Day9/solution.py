from math import prod


class HeightMap:
    def __init__(self, data: list[list[int]]) -> None:
        self.map = data
        self.h = len(self.map)
        self.w = len(self.map[0])

    def get_adj_points(self, x, y):
        adj = []

        if x > 0:
            adj.append((x - 1, y))
        if x < self.w - 1:
            adj.append((x + 1, y))
        if y > 0:
            adj.append((x, y - 1))
        if y < self.h - 1:
            adj.append((x, y + 1))

        return adj

    def get_adj_heights(self, x, y):
        return [self.map[y][x] for x, y in self.get_adj_points(x, y)]

    def get_pool_points(self, x, y, known=[]):
        adj = self.get_adj_points(x, y)
        pool = []

        for p in adj:
            if p not in known and self.map[p[1]][p[0]] < 9:
                pool.append(p)
                pool.extend(self.get_pool_points(*p, known + pool))
                pool = [p for i, p in enumerate(pool) if pool.index(p) == i]
        return pool

    def get_lowst_points(self):
        lowest = []
        for x in range(self.w):
            for y in range(self.h):
                h = self.map[y][x]
                if all([h < n for n in self.get_adj_heights(x, y)]):
                    lowest.append((x, y))
        return lowest


def parse_input(puzzle_input: str):
    data = []
    for line in puzzle_input.splitlines():
        if line != "":
            data.append([int(n) for n in line])
    return data


def solution_1(puzzle_input: str):
    data = parse_input(puzzle_input)
    h_map = HeightMap(data)
    lowest_points = h_map.get_lowst_points()
    lowest_heights = [h_map.map[y][x] for x, y in lowest_points]
    return sum(lowest_heights) + len(lowest_points)


def solution_2(puzzle_input: str):
    data = parse_input(puzzle_input)
    h_map = HeightMap(data)
    lowest_points = h_map.get_lowst_points()
    pools = sorted(
        [h_map.get_pool_points(*p) for p in lowest_points], key=len, reverse=True
    )

    return prod(len(p) for p in pools[:3])

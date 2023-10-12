import re


class Node:
    def __init__(self, x, y, size, used, avail, *args):
        self.pos = (int(x), int(y))
        self.size = int(size)
        self.used = int(used)

    @property
    def avail(self):
        return self.size - self.used


def parse_input(puzzle_input: str) -> list[Node]:
    pattern = r".*x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%"
    return [Node(*m.groups()) for m in re.finditer(pattern, puzzle_input)]


def parse_input_map(puzzle_input: str):
    pattern = r".*x(\d+)-y(\d+) +(\d+)T +(\d+)T +(\d+)T +(\d+)%"
    map, row = [], []
    cx = "0"

    for m in re.finditer(pattern, puzzle_input):
        x, y, size, used, *rest = m.groups()
        if x != cx:
            map.append(row)
            row = []
            cx = x

        row.append((int(size), int(used)))

    return map


def solution_1(puzzle_input: str):
    nodes = parse_input(puzzle_input)
    num_pairs = 0

    for n in nodes:
        for m in nodes:
            if n is not m and 0 < n.used <= m.avail:
                num_pairs += 1
    return num_pairs


def solution_2(puzzle_input: str):
    input = parse_input_map(puzzle_input)
    hole = None
    wallsize = 0
    max_x = len(input) - 1

    for x, line in enumerate(input):
        for y, n in enumerate(line):
            if n[1] == 0:
                hole = (x, y)
            if n[1] > 100:
                wallsize += 1
    if hole:
        distance_hole = hole[1] + wallsize + (wallsize - max_x + hole[0])
        return 5 * max_x + distance_hole + 1

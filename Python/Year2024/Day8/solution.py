from collections import defaultdict
from itertools import count
from typing import TypeAlias

Pos: TypeAlias = tuple[int, int]


def parse_input(aoc_input: str):
    antennas = defaultdict(list)
    map = [n for n in aoc_input.splitlines() if n != ""]

    for y, line in enumerate(aoc_input.splitlines()):
        for x, c in enumerate(line):
            if c != ".":
                antennas[c].append((x, y))

    return antennas, (len(map[0]), len(map))


def get_antinodes(antenna: list[Pos], dimensions) -> set[Pos]:
    (width, height) = dimensions
    antinodes = set()

    if len(antenna) <= 1:
        raise ValueError("Invalid number of antennas at least 2 is required")

    for i, (x1, y1) in enumerate(antenna):
        for x2, y2 in antenna[i + 1 :]:
            dx, dy = x2 - x1, y2 - y1

            nx1, ny1 = x1 - dx, y1 - dy
            if 0 <= nx1 < width and 0 <= ny1 < height:
                antinodes.add((nx1, ny1))

            nx2, ny2 = x2 + dx, y2 + dy
            if 0 <= nx2 < width and 0 <= ny2 < height:
                antinodes.add((nx2, ny2))

    return antinodes


def get_resonance_antinodes(antenna: list[Pos], dimensions) -> set[Pos]:
    (width, height) = dimensions
    anti_nodes = set()

    if len(antenna) <= 1:
        raise ValueError("Invalid number of antennas at least 2 is required")

    for i, (x1, y1) in enumerate(antenna):
        for x2, y2 in antenna[i + 1 :]:
            dx, dy = x2 - x1, y2 - y1

            for n in count(1):
                nx1, ny1 = x1 - dx * n, y1 - dy * n
                if 0 <= nx1 < width and 0 <= ny1 < height:
                    anti_nodes.add((nx1, ny1))
                else:
                    break
            for n in count(1):
                nx2, ny2 = x2 + dx * n, y2 + dy * n
                if 0 <= nx2 < width and 0 <= ny2 < height:
                    anti_nodes.add((nx2, ny2))
                else:
                    break

    return anti_nodes


def solution_1(aoc_input: str):
    antennas, dimension = parse_input(aoc_input)
    nodes = set()

    for antenna in antennas.values():
        nodes |= get_antinodes(antenna, dimension)

    return len(nodes)


def solution_2(aoc_input: str):
    antennas, dimension = parse_input(aoc_input)
    nodes = set()

    for antenna in antennas.values():
        nodes |= set(antenna)
        nodes |= get_resonance_antinodes(antenna, dimension)

    return len(nodes)

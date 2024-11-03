from enum import Enum
from typing import TypeVar, TypeAlias
import re


HEX_DIR = {"0": "R", "1": "D", "2": "L", "3": "U"}

MOVEMENT = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}

Position: TypeAlias = tuple[int, int]
Vertex: TypeAlias = tuple[str, int]


def parse_simple(aoc_input: str) -> list[Vertex]:
    vertices = []
    for match in re.finditer(r"([LDRU]) (\d+) \(#([\da-f]{6})\)", aoc_input):
        o, d, _ = match.groups()
        vertices.append((o, int(d)))
    return vertices


def parse_hex(aoc_input: str) -> list[Vertex]:
    vertices = []
    for match in re.finditer(r"([LDRU]) (\d+) \(#([\da-f]{6})\)", aoc_input):
        _, _, h = match.groups()
        l = int(h[:-1], 16)
        d = HEX_DIR[h[-1]]

        vertices.append((d, l))
    return vertices


def translate_vertices_to_pos(vertices: list[Vertex]) -> list[Position]:
    pos = [(0, 0)]
    last_pos = (0, 0)

    for orient, dist in vertices:
        dpos = [m * dist for m in MOVEMENT[orient]]
        new_pos = (last_pos[0] + dpos[0], last_pos[1] + dpos[1])
        pos.append(new_pos)
        last_pos = new_pos

    assert pos[-1] == (0, 0)
    return pos


def circumflex(vertices: list[Vertex]) -> int:
    return sum(d for _, d in vertices)


def shoelace_surface(positions: list[Position]):
    total = 0

    for n, (x1, y1) in enumerate(positions[:-1]):
        (x2, y2) = positions[n + 1]
        total += x1 * y2 - x2 * y1

    return 0.5 * abs(total)


def get_lava_capa(vertices: list[Vertex]):
    pos = translate_vertices_to_pos(vertices)
    a = shoelace_surface(pos)
    b = circumflex(vertices)
    i = a - b / 2 + 1
    return b + i


def solution_1(aoc_input: str):
    vertices = parse_simple(aoc_input)
    return get_lava_capa(vertices)


def solution_2(aoc_input: str):
    vertices = parse_hex(aoc_input)
    return get_lava_capa(vertices)

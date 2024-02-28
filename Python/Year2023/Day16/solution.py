from collections import deque
from typing import TypeAlias

Pos: TypeAlias = tuple[int, int]
Dir: TypeAlias = tuple[int, int]

REFLECTION_MAP = {
    "/": {
        (0, 1): [(-1, 0)],
        (0, -1): [(1, 0)],
        (1, 0): [(0, -1)],
        (-1, 0): [(0, 1)],
    },
    "\\": {
        (0, 1): [(1, 0)],
        (0, -1): [(-1, 0)],
        (1, 0): [(0, 1)],
        (-1, 0): [(0, -1)],
    },
    "|": {
        (0, 1): [(0, 1)],
        (0, -1): [(0, -1)],
        (1, 0): [(0, 1), (0, -1)],
        (-1, 0): [(0, 1), (0, -1)],
    },
    "-": {
        (0, 1): [(1, 0), (-1, 0)],
        (0, -1): [(1, 0), (-1, 0)],
        (1, 0): [(1, 0)],
        (-1, 0): [(-1, 0)],
    },
}


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def get_all_start_pos(beam_map: list[str]) -> list[tuple[Pos, Dir]]:
    lx, ly = len(beam_map[0]), len(beam_map)
    starts = []

    # top facing down
    for x in range(lx):
        starts.append(((x, -1), (0, 1)))
    # bottom facing up
    for x in range(lx):
        starts.append(((x, ly), (0, -1)))
    # left facing right
    for y in range(ly):
        starts.append(((-1, y), (1, 0)))
    # right facing left
    for y in range(ly):
        starts.append(((lx, y), (-1, 0)))

    return starts


def get_reflections(direction: Dir, field: str) -> list[Dir]:
    if field in REFLECTION_MAP:
        return REFLECTION_MAP[field][direction]
    else:
        return [direction]


def get_num_energized(start_pos: Pos, start_dir: Dir, beam_map: list[str]) -> int:
    lx, ly = len(beam_map[0]), len(beam_map)
    known_beams: set[tuple[Pos, Dir]] = set()
    q = deque([(start_pos, start_dir)])

    while q:
        pos, direct = q.popleft()
        nx, ny = pos[0] + direct[0], pos[1] + direct[1]

        if 0 <= nx < lx and 0 <= ny < ly:
            for ndir in get_reflections(direct, beam_map[ny][nx]):
                beam_pos = ((nx, ny), ndir)
                if beam_pos not in known_beams:
                    q.append(beam_pos)
                    known_beams.add(beam_pos)

    energized = set(pos for pos, direct in known_beams)
    return len(energized)


def solution_1(aoc_input: str):
    beam_map = parse_input(aoc_input)
    return get_num_energized((-1, 0), (1, 0), beam_map)


def solution_2(aoc_input: str):
    beam_map = parse_input(aoc_input)
    return max(
        get_num_energized(s, d, beam_map) for s, d in get_all_start_pos(beam_map)
    )

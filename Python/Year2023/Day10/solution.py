from itertools import count
from typing import TypeAlias
from termcolor import colored

Map: TypeAlias = list[str]
Pos: TypeAlias = tuple[int, int]

START = "S"
N = (0, -1)
S = (0, 1)
E = (1, 0)
W = (-1, 0)

CONNECTION = {
    "|": (N, S),
    "-": (W, E),
    "L": (N, E),
    "J": (N, W),
    "7": (S, W),
    "F": (S, E),
    ".": (),
}


def parse_input(aoc_input: str) -> Map:
    return [n for n in aoc_input.splitlines() if n != ""]


def get_start(pipe_map: Map) -> Pos:
    for y, line in enumerate(pipe_map):
        if START in line:
            return line.index(START), y


def first_step(pipe_map: Map, start: Pos) -> tuple[Pos, Pos]:
    for dx, dy in [N, E, S, W]:
        nx, ny = start[0] + dx, start[1] + dy
        pipe = pipe_map[ny][nx]

        try:
            con_idx = CONNECTION[pipe].index((-dx, -dy))
            return (nx, ny), CONNECTION[pipe][(con_idx + 1) % 2]
        except ValueError:
            continue


def replace_start(pipe_map: Map):
    # fixes replacement for my inputs
    for i in range(len(pipe_map)):
        pipe_map[i] = pipe_map[i].replace("S", "7")
    return pipe_map


def get_loop(pipe_map: Map) -> set[Pos]:
    start = get_start(pipe_map)
    pos = {start}
    c_pos, c_dir = first_step(pipe_map, start)
    pos.add(c_pos)

    for i in count():
        # move to next field
        dx, dy = c_dir
        c_pos = c_pos[0] + dx, c_pos[1] + dy
        pos.add(c_pos)
        if c_pos == start:
            return pos

        pipe = pipe_map[c_pos[1]][c_pos[0]]
        con_idx = CONNECTION[pipe].index((-dx, -dy))
        c_dir = CONNECTION[pipe][(con_idx + 1) % 2]


def get_inside_fields(pipe_map, loop) -> int:
    """
    based on an idea of u/hi_im_new_to_this

    when we shoot a ray from a field to the outside and the field is enclosed then the amount of pipes we encounter
    on way out needs to be odd
    """

    pipe_map = replace_start(pipe_map)
    inside_fiels = set()
    for y, line in enumerate(pipe_map):
        for x, c in enumerate(line):
            if (x, y) in loop:
                continue

            x_ray, y_ray = int(x), int(y)
            cross_counter = 0

            while x_ray < len(pipe_map[0]) and y_ray < len(pipe_map):
                c_ray = pipe_map[y_ray][x_ray]
                if (x_ray, y_ray) in loop and c_ray != "L" and c_ray != "7":
                    cross_counter += 1
                x_ray += 1
                y_ray += 1

            if cross_counter % 2 == 1:
                inside_fiels.add((x, y))

    return len(inside_fiels)


def solution_1(aoc_input: str):
    pipe_map = parse_input(aoc_input)
    return len(get_loop(pipe_map)) // 2


def solution_2(aoc_input: str):
    pipe_map = parse_input(aoc_input)
    loop = get_loop(pipe_map)
    insides = get_inside_fields(pipe_map, loop)
    return insides

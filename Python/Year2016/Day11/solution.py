import re
from copy import deepcopy
from itertools import chain, combinations
from queue import PriorityQueue


def parse_floors(aoc_input):
    floors = []
    for line in aoc_input.replace("-compatible", "").splitlines():
        floors.append(
            list(m.groups() for m in re.finditer(r"(\w+) (generator|microchip)", line))
        )
    return floors


def dist(floors):
    return sum([len(f) * (len(floors) - 1 - i) for i, f in enumerate(floors)])


def hashable(floors):
    hash_floor = []

    for f in floors:
        fstr = "".join(e[1] for e in sorted(f))
        hash_floor.append(fstr)

    return tuple(hash_floor)


def valid_floor(floor):
    chips = {n[0] for n in floor if n[1] == "microchip"}
    gen = {n[0] for n in floor if n[1] == "generator"}

    return not chips.difference(gen) or not gen


def valid_floors(floors):
    return all(valid_floor(f) for f in floors)


def gen_next_floors(floor, elevator):
    for d_elevator in (1, -1):
        if not 0 <= elevator + d_elevator <= len(floor) - 1:
            continue

        for move in chain.from_iterable(
            combinations(floor[elevator], c) for c in [2, 1]
        ):
            n_floors = deepcopy(floor)
            n_floors[elevator] = [n for n in n_floors[elevator] if n not in move]
            n_floors[elevator + d_elevator] = [*n_floors[elevator + d_elevator], *move]
            if valid_floors(n_floors):
                yield n_floors, elevator + d_elevator


def gen_next_floors_v2(floors, elevator):
    pass


def get_nums_move(floors):
    q = PriorityQueue()
    q.put((dist(floors), 0, 0, floors))
    visited = {(0, hashable(floors))}

    while q:
        _, c_ele, c_moves, c_floors = q.get()
        pass
        for next_floors, next_elevator in gen_next_floors(c_floors, c_ele):
            if dist(next_floors) == 0:
                return c_moves + 1
            if (next_elevator, hashable(next_floors)) not in visited:
                visited.add((next_elevator, hashable(next_floors)))
                q.put(
                    (
                        c_moves + 1 + dist(next_floors),
                        next_elevator,
                        c_moves + 1,
                        next_floors,
                    )
                )


def solution_1(aoc_input):
    floors = parse_floors(aoc_input)
    return get_nums_move(floors)


def solution_2(aoc_input):
    floors = parse_floors(aoc_input)
    floors[0] += [
        ("elerium", "generator"),
        ("elerium", "microchip"),
        ("dilithium", "generator"),
        ("dilithium", "microchip"),
    ]
    return get_nums_move(floors)

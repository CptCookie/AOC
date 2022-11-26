from typing import Callable


def parse_data(puzzle_input: str) -> list[int]:
    return [int(n) for n in puzzle_input.splitlines() if n != ""]


def n_septs_to_leave(instr: list[int], delta_jump: Callable[[int], int]) -> int:
    counter = 0
    pos = 0
    while pos < len(instr):
        new_pos = pos + instr[pos]
        instr[pos] += delta_jump(instr[pos])
        counter += 1
        pos = new_pos

    return counter


def solution_1(puzzle_input: str):
    instr = parse_data(puzzle_input)
    return n_septs_to_leave(instr, lambda x: 1)


def solution_2(puzzle_input: str):
    instr = parse_data(puzzle_input)
    return n_septs_to_leave(instr, lambda x: -1 if x >= 3 else 1)

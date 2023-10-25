from copy import deepcopy
from typing import Iterable

from Year2016.assembunny import AssemBunnyComputer, LoopException


def parse_input(puzzle_input: str) -> list[list[str]]:
    instr = []
    for line in puzzle_input.splitlines():
        if line != "":
            instr.append([c if c.isalpha() else int(c) for c in line.split()])
    return instr


def is_alternating(a: Iterable[int]):
    return all(n == 0 if i % 2 == 0 else n == 1 for i, n in enumerate(a))


def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    init_a = 0
    print(input)
    while True:
        bunny_pc = AssemBunnyComputer(deepcopy(input))
        bunny_pc["a"] = init_a
        try:
            bunny_pc.run_instr()
        except LoopException:
            if is_alternating(bunny_pc.output):
                return init_a

        init_a += 1


def solution_2(puzzle_input: str):
    return "Merry Chistmas"

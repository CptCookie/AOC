from collections import defaultdict
import re
from typing import Tuple
from operator import __ge__, __gt__, __eq__, __ne__, __lt__, __le__

COMPARISONS = {
    "==": __eq__,
    "!=": __ne__,
    "<": __lt__,
    "<=": __le__,
    ">": __gt__,
    ">=": __ge__,
}


def parse_data(puzzle_input: str) -> list[str]:
    regex = r"([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) ([!><=]+) (-?\d+)"
    return re.findall(regex, puzzle_input)


class Memory:
    def __init__(self):
        self.registers = defaultdict(lambda: 0)

    @property
    def max(self):
        return max(self.registers.values())

    def execute(self, instruction: Tuple[str, str, str, str, str, str]):
        condition = instruction[3:]
        operation = instruction[:3]

        if self.eval_condition(*condition):
            value = int(operation[2])
            if operation[1] == "dec":
                value = value * -1
            self.registers[operation[0]] += value

    def eval_condition(self, reg, op, value) -> bool:
        return COMPARISONS[op](self.registers[reg], int(value))


def solution_1(puzzle_input: str) -> int:
    mem = Memory()
    instr = parse_data(puzzle_input)
    for i in instr:
        mem.execute(i)

    return mem.max


def solution_2(puzzle_input: str) -> int:
    mem = Memory()
    max_val = 0
    instr = parse_data(puzzle_input)
    for i in instr:
        mem.execute(i)
        max_val = max(mem.max, max_val)
    return max_val

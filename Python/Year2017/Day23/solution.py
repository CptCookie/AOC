import math
from collections import defaultdict
from copy import deepcopy


class Processor:
    def __init__(self, instuctions):
        self.registers = defaultdict(lambda: 0)
        self.instructions = instuctions
        self.pc = 0
        self.mul_count = 0

    def _get_value(self, address: str) -> int:
        if address.isalpha():
            return self.registers[address]
        else:
            return int(address)

    def set(self, x, y):
        self.registers[x] = self._get_value(y)
        self.pc += 1

    def sub(self, x, y):
        self.registers[x] -= self._get_value(y)
        self.pc += 1

    def mul(self, x, y):
        self.registers[x] *= self._get_value(y)
        self.mul_count += 1
        self.pc += 1

    def jnz(self, x, y):
        if self._get_value(x) != 0:
            self.pc += self._get_value(y)

        else:
            self.pc += 1

    def execute(self):
        while self.pc < len(self.instructions):
            match self.instructions[self.pc].split(" "):
                case "set", x, y:
                    self.set(x, y)
                case "sub", x, y:
                    self.sub(x, y)
                case "mul", x, y:
                    self.mul(x, y)
                    self.registers["mul_counter"] += 1
                case "jnz", x, y:
                    self.jnz(x, y)


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False

    r = int(n**0.5)
    # since all primes > 3 are of the form 6n ± 1
    # start with f=5 (which is prime)
    # and test f, f+2 for being prime
    # then loop by 6.
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


def solution_1(aoc_input: str):
    instr = parse_input(aoc_input)
    cpu = Processor(instr)
    cpu.execute()
    return cpu.mul_count


def solution_2(aoc_input: str):
    instr = parse_input(aoc_input)
    cpu = Processor(instr[:8])
    cpu.registers["a"] = 1
    cpu.execute()
    h = 0

    for b in range(cpu.registers["b"], cpu.registers["c"] + 1, 17):
        if not is_prime(b):
            h += 1

    return h

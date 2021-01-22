from copy import deepcopy
import re


class Programm:
    def __init__(self, instructions):
        self.instr = [n.replace("-> ", "").split(" ") for n in instructions]
        for n, elem in enumerate(self.instr):
            self.instr[n] = [int(m) if re.match(r"\d", m) else m for m in elem]
        self.mem = {}

    def _set(self, key, value):
        if type(value) == str and value in self.mem:
            self.mem.update({key: self.mem[value]})
            return True
        elif type(value) == int:
            self.mem.update({key: value})
            return True

    def _not(self, arg, to: str):
        if type(arg) == str and arg in self.mem:
            self.mem.update({to: 65535 - self.mem[arg]})
            return True
        elif type(arg) == int:
            self.mem.update({to: 65535 - arg})
            return True

    def _and(self, arg_1: str, arg_2: str, to: str):
        if type(arg_1) == str and arg_1 in self.mem and arg_2 in self.mem:
            self.mem.update({to: self.mem[arg_1] & self.mem[arg_2]})
            return True
        elif type(arg_1) == int and arg_2 in self.mem:
            self.mem.update({to: arg_1 & self.mem[arg_2]})
            return True

    def _or(self, arg_1: str, arg_2: str, to: str):
        if type(arg_1) == str and arg_1 in self.mem and arg_2 in self.mem:
            self.mem.update({to: self.mem[arg_1] | self.mem[arg_2]})
            return True
        elif type(arg_1) == int and arg_2 in self.mem:
            self.mem.update({to: arg_1 | self.mem[arg_2]})
            return True

    def _lshift(self, addr: str, number: int, to: str):
        if addr in self.mem:
            self.mem.update({to: self.mem[addr] << number})
            return True

    def _rshift(self, addr: str, number: int, to: str):
        if addr in self.mem:
            self.mem.update({to: self.mem[addr] >> number})
            return True

    def run(self):
        while len(self.instr) > 0:
            buffer_instr = deepcopy(self.instr)

            for n, line in enumerate(self.instr):
                executed = False
                if len(line) == 2:
                    executed = self._set(line[1], line[0])
                elif len(line) == 3 and line[0] == "NOT":
                    executed = self._not(line[1], line[2])
                elif line[1] == "RSHIFT":
                    executed = self._rshift(line[0], line[2], line[3])
                elif line[1] == "LSHIFT":
                    executed = self._lshift(line[0], line[2], line[3])
                elif line[1] == "AND":
                    executed = self._and(line[0], line[2], line[3])
                elif line[1] == "OR" and line[0]:
                    executed = self._or(line[0], line[2], line[3])
                if executed:
                    buffer_instr.pop(n)
                    break

            if len(buffer_instr) == 0:
                return
            elif len(buffer_instr) == len(self.instr):
                raise Exception("Can not resolve all Instructions")
            else:
                self.instr = buffer_instr


def solution_1(puzzle_input):
    prog = Programm([n for n in puzzle_input.split("\n") if n != ""])
    prog.run()
    return prog.mem["a"]


def solution_2(puzzle_input):
    prog = Programm([n for n in puzzle_input.split("\n") if n != ""])
    prog.run()
    a = prog.mem["a"]

    instr = [n for n in puzzle_input.split("\n") if n != ""]
    for n, line in enumerate(instr):
        if re.match("\d+ -> b", line):
            instr[n] = f"{a} -> b"

    prog = Programm(instr)
    prog.run()
    return prog.mem["a"]

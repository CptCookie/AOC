from typing import Sequence


MOVES = {
    "U": (0, -1),
    "R": (1, 0),
    "D": (0, 1),
    "L": (-1, 0),
}


def add_tuples(tuple_1, tuple_2):
    return [sum(i) for i in zip(tuple_1, tuple_2)]


class NumberCode:
    PAD = [("1", "2", "3"), ("4", "5", "6"), ("7", "8", "9")]
    start = [1, 1]

    def __init__(self):
        self.dimension = len(self.PAD)
        self.pos = self.start

    @property
    def number(self):
        return self.PAD[self.pos[1]][self.pos[0]]

    def move(self, dir):
        new_pos = add_tuples(self.pos, MOVES[dir])
        if 0 <= new_pos[0] < self.dimension and 0 <= new_pos[1] < self.dimension:
            new_value = self.PAD[new_pos[1]][new_pos[0]]
            if new_value != "X":
                self.pos = new_pos

    def decode_number(self, code: str):
        for i in code:
            self.move(i)


class RombicCode(NumberCode):
    PAD = [
        ["X", "X", "1", "X", "X"],
        ["X", "2", "3", "4", "X"],
        ["5", "6", "7", "8", "9"],
        ["X", "A", "B", "C", "X"],
        ["X", "X", "D", "X", "X"],
    ]
    start = [2, 2]


def parse_input(puzzle_input):
    return [n for n in puzzle_input.splitlines() if n is not ""]


def solution_1(puzzle_input: str):
    puzzle_input = parse_input(puzzle_input)
    code = NumberCode()
    sequence = []
    for line in puzzle_input:
        code.decode_number(line)
        sequence.append(code.number)
    return "".join(sequence)


def solution_2(puzzle_input):
    puzzle_input = parse_input(puzzle_input)
    code = RombicCode()
    sequence = []
    for line in puzzle_input:
        code.decode_number(line)
        sequence.append(code.number)
    return "".join(sequence)
import re


def parse_input(aoc_input: str) -> list[str]:
    instructions = []
    pattern = r"(L|R)(\d+)"
    for match in re.finditer(pattern, aoc_input):
        (d, l) = match.groups()
        instructions.append((d, int(l)))
    return instructions


class Dial:
    def __init__(self):
        self.number = 50
        self.zero_cnt = 0
        self.zero_pass_cnt = 0

    def turn(self, direction, num):
        if direction == "L":
            self.turn_left(num)
        else:
            self.turn_right(num)

    def turn_left(self, num):
        rotations = num // 100
        self.zero_pass_cnt += rotations

        if num % 100 == self.number:
            self.zero_cnt += 1

        if num % 100 > self.number and self.number != 0:
            self.zero_pass_cnt += 1

        self.number = (self.number - num) % 100

    def turn_right(self, num):
        rotations = num // 100
        self.zero_pass_cnt += rotations

        if num % 100 == 100 - self.number:
            self.zero_cnt += 1

        if num % 100 > 100 - self.number and self.number != 0:
            self.zero_pass_cnt += 1

        self.number = (self.number + num) % 100


def solution_1(aoc_input: str):
    safe = Dial()
    instructions = parse_input(aoc_input)
    for d, l in instructions:
        safe.turn(d, l)

    return safe.zero_cnt


def solution_2(aoc_input: str):
    safe = Dial()
    instructions = parse_input(aoc_input)
    for d, l in instructions:
        safe.turn(d, l)

    return safe.zero_pass_cnt + safe.zero_cnt

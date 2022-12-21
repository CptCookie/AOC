import re
from operator import mul, add, sub, floordiv, eq
class NumMonkey:
    def __init__(self, name, value):
        self.name = name
        self.value = int(value)

    def contains_humn(self):
        return self.name == "humn"

    def set_value(self, value):
        if self.name == "humn":
            self.value = value
        else:
            raise AttributeError("Can only edit values of Humans")

class OpMonkey:
    OPS = {
        "+" : add,
        "-": sub,
        "*": mul,
        "/": floordiv,
        "=": eq
        }

    INV_OPS = {
        "+": sub,
        "-": add,
        "*": floordiv,
        "/": mul,
        }
    def __init__(self, name, operator, left, right):
        self.name = name
        self.operator = operator
        self.left = left
        self.right = right

    @property
    def value(self):
        return self.OPS[self.operator](self.left.value, self.right.value)

    def contains_humn(self):
        return self.left.contains_humn() or self.right.contains_humn()

    def set_value(self, value):
        """
        value = left op right
        => left = value op^-1 right
        """
        left_humn = self.left.contains_humn()

        if left_humn:
            # calc with inverted operator works for all
            self.left.set_value(self.INV_OPS[self.operator](value, self.right.value))
        elif self.operator in ["+", "*"]:
            # calc with inverted operator works for not directed operations
            self.right.set_value(self.INV_OPS[self.operator](value, self.left.value))
        else:
            # calc for not directed operations
            self.right.set_value(self.OPS[self.operator](self.left.value, value))

    def balance_values(self):
        left_humn = self.left.contains_humn()

        if left_humn:
            self.left.set_value(self.right.value)
        else:
            self.right.set_value(self.left.value)



def parse_input(puzzle_input: str) -> list[str]:
    pattern = r"([a-z]{4}): (\d+)|([a-z]{4}): ([a-z]{4}) ([*+\-\/]{1}) ([a-z]{4})"
    monkeys = {}

    while "root" not in monkeys:
        for group in re.findall(pattern, puzzle_input):
            if group[0] not in monkeys:
                if group[0] != "":
                    monkeys[group[0]] = NumMonkey(group[0], group[1])
                if group[2] != "" and group[3] in monkeys and group[5] in monkeys:
                    monkeys[group[2]] = OpMonkey(group[2], group[4], monkeys[group[3]], monkeys[group[5]])

    return monkeys["root"], monkeys["humn"]


def solution_1(puzzle_input: str):
    root, _ = parse_input(puzzle_input)
    return root.value


def solution_2(puzzle_input: str):
    root, you = parse_input(puzzle_input)
    root.balance_values()
    return you.value


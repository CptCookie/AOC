import re
from collections import OrderedDict
from operator import mul
from functools import reduce


class Monkey:
    def __init__(self, items, operation, division, true, false):
        self.items = items
        self.operation = operation
        self.division = division
        self.true = true
        self.false = false
        self.inspected = 0
        self.manage_worry = lambda x: x // 3

    def __repr__(self) -> str:
        return f"{self.items}"

    def new_value(self, value: int, operation: str) -> int:
        op_result = eval(operation.replace("old", f"{value}"))
        return self.manage_worry(op_result)


def parse_data(puzzle_input: str, level_2: bool = False) -> OrderedDict[Monkey]:
    monkeys = OrderedDict()
    pattern = r"(Monkey \d+):\n.+: ([\d\, ]+)\n.+: new = (old [\*\+] [\d\w]+)\n.+by (\d+)\n.+(monkey \d+)\n.+(monkey \d+)"
    for m in [re.findall(pattern, n) for n in puzzle_input.split("\n\n") if n != ""]:
        name, items, operation, divisible, true, false = m[0]
        items = [int(i) for i in items.split(",")]
        divisible = int(divisible)
        m = Monkey(items, operation, divisible, true, false)

        monkeys[name.lower()] = m

    if level_2:
        new_manage_value = reduce(mul, (m.division for m in monkeys.values()))
        for m in monkeys.values():
            m.manage_worry = lambda x: x % new_manage_value

    return monkeys


def run_round(monkeys):
    for m in monkeys.values():
        run_monkey(m, monkeys)


def run_monkey(monkey: Monkey, all_monkeys: OrderedDict[str, Monkey]):
    for i in monkey.items:
        monkey.inspected += 1
        new_value = monkey.new_value(i, monkey.operation)
        if new_value % monkey.division == 0:
            all_monkeys[monkey.true].items.append(new_value)
        else:
            all_monkeys[monkey.false].items.append(new_value)
    monkey.items = []


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    for _ in range(20):
        run_round(data)

    insp = sorted([n.inspected for n in data.values()], reverse=True)
    return insp[0] * insp[1]


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input, True)

    for _ in range(10000):
        run_round(data)

    insp = sorted([n.inspected for n in data.values()], reverse=True)
    return insp[0] * insp[1]

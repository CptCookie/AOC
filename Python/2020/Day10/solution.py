from const import token
from itertools import chain, combinations


def get_differnces(adapters: [int]):
    dif = [0, 0, 0]
    for n, elem in enumerate(adapters[1:]):
        dif[elem - adapters[n] - 1] += 1
    return dif


def number_valid_combinations(adapters):
    counter = 0
    combinations = 1
    combos = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    for n, adapt in enumerate(adapters[1:]):
        if adapt - adapters[n] == 1:
            counter += 1
        else:  # ccccombo bracker
            combinations *= combos[counter]
            counter = 0
    return combinations


def solve(puzzle_input):
    adapters = sorted([int(n) for n in puzzle_input.split("\n") if n != ""])
    dif = get_differnces([0] + adapters + [max(adapters) + 3])
    print(f"solution 1: {dif[0] * dif[2]}")
    print(
        f"solution 2: {number_valid_combinations([0] + adapters + [max(adapters)+3])}"
    )

from itertools import combinations
from math import prod
from typing import List


def get_solution(gifts_weigts: List[int], storages: int):
    for numbers in range(1, int(len(gifts_weigts) / storages) + 1):
        solutions = sorted(
            prod(i)
            for i in combinations(gifts_weigts, numbers)
            if sum(i) == sum(gifts_weigts) / storages
        )
        if len(solutions) > 0:
            return solutions[0]


def solution_1(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.splitlines() if n != ""]
    return get_solution(puzzle_input, 3)


def solution_2(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.splitlines() if n != ""]
    return get_solution(puzzle_input, 4)

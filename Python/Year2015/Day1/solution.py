from typing import List, Union

UP = 1
DOWN = -1
Stair = int


def last_floor(stairs: str):
    return sum(stairs)


def find_floor(stairs: List[Stair], target_floor: int) -> int:
    current_floor = 0
    for n, current_stair in enumerate(stairs):
        current_floor += current_stair
        if current_floor == target_floor:
            return n


def parse_stairs(puzzle_string: str) -> List[Stair]:
    stairs = [UP if n == "(" else DOWN for n in puzzle_string]
    return stairs


def solution_1(puzzle_string):
    stairs = parse_stairs(puzzle_string)
    return last_floor(stairs)


def solution_2(puzzle_string):
    stairs = parse_stairs(puzzle_string)
    return find_floor(stairs, 0) + 1

from collections import namedtuple
from typing import Iterable

UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"

Position = namedtuple("Position", ["x", "y"])


def get_all_pos(puzzel_input: str) -> Iterable[Position]:
    all_pos = [Position(0, 0)]

    for direction in puzzel_input:
        current_pos = all_pos[-1]

        if direction is UP:
            all_pos.append(Position(current_pos.x, current_pos.y + 1))

        elif direction is DOWN:
            all_pos.append(Position(current_pos.x, current_pos.y - 1))

        elif direction is RIGHT:
            all_pos.append(Position(current_pos.x + 1, current_pos.y))

        elif direction is LEFT:
            all_pos.append(Position(current_pos.x - 1, current_pos.y))

    return all_pos


def get_unique(elements: Iterable) -> Iterable:
    return [e for n, e in enumerate(elements) if elements.index(e) == n]


def solution_1(moves) -> int:
    return len(get_unique(get_all_pos(moves)))


def solution_2(moves) -> int:
    santa_moves = moves[::2]
    santa_positions = get_all_pos(santa_moves)

    robot_moves = moves[1::2]
    robot_positions = get_all_pos(robot_moves)

    return len(get_unique(santa_positions + robot_positions))

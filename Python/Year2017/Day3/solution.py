from collections import defaultdict
from typing import Tuple

"""
37  36  35  34  33  32  31
38  17  16  15  14  13  30
39  18   5   4   3  12  29
40  19   6   1   2  11  28   ^
41  20   7   8   9  10  27   |
42  21  22  23  24  25  26   |
43  44  45  46  47  48  49  50
"""


def parse_data(puzzle_input: str) -> int:
    return int(puzzle_input.strip())


def get_side_length(layer):
    return 2 * layer - 1


def get_perimiter_of_layer(layer):
    if layer == 1:
        return 1
    else:
        # sidelength s = 1, 3, 5, 7, ... = (2n - 1)
        # permitier = 1, 8, 16, 24 = (4s - 4) = 8(n-1)
        return 8 * (layer - 1)


def get_start_number_of_layer(layer):
    return sum([get_perimiter_of_layer(l) for l in range(1, layer)]) + 1


def get_adjacent_positions(x, y):
    pos = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                pos.append((x + dx, y + dy))
    return pos


def get_position(address: int) -> Tuple[int, int]:
    x, y = 0, 0
    layer = 1

    if address == 1:
        return 0, 0

    for step in range(2, address + 1):
        current_layer_start = get_start_number_of_layer(layer)
        next_layer_start = get_start_number_of_layer(layer + 1)
        side_length = get_side_length(layer)

        if step == next_layer_start:
            # next layer
            x += 1
            layer += 1

        # layer 3, number 12, corner 13, start 10
        elif step <= current_layer_start + side_length - 2:
            y += 1

        # layer 3, number 15, corner 17, start 10, side_length 5
        elif (
            current_layer_start + side_length - 2
            < step
            <= current_layer_start + 2 * side_length - 3
        ):
            x -= 1

        # layer 3, number 19, corner 21, start 10, side_length 5
        elif (
            current_layer_start + 2 * side_length - 3
            < step
            <= current_layer_start + 3 * side_length - 4
        ):
            y -= 1

        # layer 3, number 23, corner 25, start 10, side_length 5
        elif (
            current_layer_start + 3 * side_length - 4
            <= step
            <= current_layer_start + 4 * side_length - 5
        ):
            x += 1

    return x, y


def get_bigger_value(limit: int) -> int:
    values = defaultdict(lambda: 0)
    x, y = 0, 0
    values[(0, 0)] = 1
    layer = 1
    step = 1

    while True:
        step += 1
        current_layer_start = get_start_number_of_layer(layer)
        next_layer_start = get_start_number_of_layer(layer + 1)
        side_length = get_side_length(layer)
        value = 0

        if step == next_layer_start:
            # next layer
            x += 1
            layer += 1

        # layer 3, number 12, corner 13, start 10
        elif step <= current_layer_start + side_length - 2:
            y += 1

        # layer 3, number 15, corner 17, start 10, side_length 5
        elif (
            current_layer_start + side_length - 2
            < step
            <= current_layer_start + 2 * side_length - 3
        ):
            x -= 1

        # layer 3, number 19, corner 21, start 10, side_length 5
        elif (
            current_layer_start + 2 * side_length - 3
            < step
            <= current_layer_start + 3 * side_length - 4
        ):
            y -= 1

        # layer 3, number 23, corner 25, start 10, side_length 5
        elif (
            current_layer_start + 3 * side_length - 4
            <= step
            <= current_layer_start + 4 * side_length - 5
        ):
            x += 1

        for pos_x, pos_y in get_adjacent_positions(x, y):
            value += values[(pos_x, pos_y)]
        values[(x, y)] = value

        if value > limit:
            return value


def solution_1(puzzle_input: str):
    address = parse_data(puzzle_input)
    (
        x,
        y,
    ) = get_position(address)
    return abs(x) + abs(y)


def solution_2(puzzle_input: str):
    address = parse_data(puzzle_input)
    return get_bigger_value(address)

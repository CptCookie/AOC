from functools import reduce
from operator import mul
import re
from typing import Dict, List, Tuple, Union, Set

input_pattern = r"value (\d+).+(bot \d+)"
hand_over_pattern = r"(bot \d+).+(bot \d+|output \d+).+(bot \d+|output \d+)"


def parse_instr(string: str):
    instr = []

    for line in string.splitlines():
        if re.search(input_pattern, line):
            instr.append(re.search(input_pattern, line).groups())
        elif re.search(hand_over_pattern, line):
            instr.append(re.search(hand_over_pattern, line).groups())

    return instr


def input_chips(instructions):
    bots = {}
    chip_inputs = [n for n in instructions if len(n) == 2]
    for i in chip_inputs:
        bots[i[1]] = bots.get(i[1], []) + [int(i[0])]
    return bots


def handle_chips(instructions, bots):
    handle_instructions = [i for i in instructions if len(i) == 3]

    while handle_instructions:
        remaining_instr = []
        for instr in handle_instructions:
            if len(bots.get(instr[0], {})) == 2:
                bots = hand_over(instr, bots)
            else:
                remaining_instr.append(instr)
        handle_instructions = remaining_instr

    return bots


def hand_over(instruction, bots):
    giver, receiver_1, receiver_2 = instruction

    bots[receiver_1] = bots.get(receiver_1, []) + [min(bots[giver])]
    bots[receiver_2] = bots.get(receiver_2, []) + [max(bots[giver])]

    return bots


def solution_1(puzzle_input: str):
    instr = parse_instr(puzzle_input)
    bots = input_chips(instr)
    bots = handle_chips(instr, bots)

    for k in bots:
        if 61 in bots[k] and 17 in bots[k]:
            return k


def solution_2(puzzle_input: str):
    instr = parse_instr(puzzle_input)
    bots = input_chips(instr)
    bots = handle_chips(instr, bots)

    return reduce(mul, bots["output 0"] + bots["output 1"] + bots["output 2"])

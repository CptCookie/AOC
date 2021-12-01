import re
from typing import Dict, List, Tuple, Union, Set

input_pattern = r"value (\d+).(bot \d+)"
hand_over_pattern = r"(bot \d+).(bot|output \d+).(bot|output \d+)"


def sort_chips(instructions):
    inventory = input_chips(instructions)


def parse_instr(string: str):
    instr = []

    for line in string.splitlines():
        if re.search(input_pattern, line):
            instr.append(re.search(input_pattern, line).groups())
        elif re.search(hand_over_pattern, line):
            instr.append(re.search(hand_over_pattern, line).groups())

    return instr


def input_chips(instructions, bots):
    chip_inputs = [n[0] for n in instructions if len(n) == 2]
    for i in chip_inputs:
        bots[i[1]] = {i[0]}
    return bots


def handle_chips(instructions, bots):
    handle_instructions = [i for i in instructions if len(i) > 3]

    while instructions:
        remaining_instr = []
        for instr in handle_instructions:
            if len(bots.get(instr[0], {})) == 2:
                bots = hand_over(instr, bots)
            else:
                remaining_instr.append(instr)
        instructions = remaining_instr


def hand_over(instruction, bots):
    giver, receiver_1, receiver_2 = instruction

    bots[receiver_1] = bots.get(receiver_1, set())
    bots[receiver_1].add(min(bots[giver]))
    bots[receiver_2] = bots.get(receiver_2, set())
    bots[receiver_2].add(max(bots[giver]))

    return bots


def solution_1(puzzle_input: str):
    return None


def solution_2(puzzle_input: str):
    return None

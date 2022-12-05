from copy import deepcopy
import re


def parse_data(puzzle_input: str):
    lines, moves = puzzle_input.split("\n\n")
    lines = [l[1::4] for l in lines.splitlines()][:-1:]

    stacks = [list(reversed([l[n] for l in lines if l[n] != " "])) for n in range(9)]
    moves = [[int(v) for v in l] for l in re.findall(r".+(\d+).+(\d+).+(\d+)", moves)]

    return stacks, moves


def move_crates(og_stack: list[list[str]], amount: int, from_idx: int, to_idx: int):
    stack = deepcopy(og_stack)
    for n in range(amount):
        if len(stack[from_idx - 1]) > 0:
            transfer = stack[from_idx - 1].pop()
            stack[to_idx - 1].append(transfer)
    return stack


def solution_1(puzzle_input: str):
    stacks, moves = parse_data(puzzle_input)
    for s in stacks:
        print(s)

    for m in moves[:1]:
        print("move", m)
        stacks = move_crates(stacks, *m)

        for s in stacks:
            print(s)
    return "".join([l[-1] if len(l) > 0 else "" for l in stacks])


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    return None

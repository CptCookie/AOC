from copy import deepcopy
import re


def parse_data(puzzle_input: str):
    lines, moves = puzzle_input.split("\n\n")
    lines = [l[1::4] for l in lines.splitlines()][:-1:]

    stacks = [list(reversed([l[n] for l in lines if l[n] != " "])) for n in range(9)]
    moves = [[int(v) for v in l] for l in re.findall(r"move (\d+) from (\d+) to (\d+)", moves)]

    return stacks, moves


def move_crates( stack: list[list[str ] ], amount: int, from_idx: int, to_idx: int ):
    for _ in range( amount ):
        stack[ to_idx - 1 ].append( stack[ from_idx - 1 ].pop() )
    return stack

def solution_1(puzzle_input: str):
    stacks, moves = parse_data( puzzle_input )
    for m in moves:
        move_crates(stacks, *m)

    return( "".join( [ s.pop() for s in stacks ] ) )




def solution_2(puzzle_input: str):
    pass
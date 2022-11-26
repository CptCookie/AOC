def parse_data(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.strip().split(",") if n != "\n"]


"""
    -r      q    
      \.n  /
    nw +--+ ne
      /    \.
  s -+      +- -s
      \.   /
    sw +--+ se
      / s  \.
    -q      r

    (q,r,s)
"""


DIRECTIONS = {
    "n": (1, -1, 0),
    "ne": (1, 0, -1),
    "se": (0, 1, -1),
    "s": (-1, 1, 0),
    "sw": (-1, 0, 1),
    "nw": (0, -1, 1),
}


def move_hex(moves: list[str]) -> tuple[int, int, int]:
    pos = [(0, 0, 0)]

    for m in moves:
        moving = DIRECTIONS[m]
        pos.append(tuple(sum(z) for z in zip(pos[-1], moving)))
    return pos


def distance(pos: tuple[int, int, int]) -> int:
    return sum(abs(p) for p in pos) / 2


def solution_1(puzzle_input: str):
    moves = parse_data(puzzle_input)
    pos = move_hex(moves)
    return distance(pos[-1])


def solution_2(puzzle_input: str):
    moves = parse_data(puzzle_input)
    pos = move_hex(moves)
    return max(distance(p) for p in pos)

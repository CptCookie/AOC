from functools import reduce
from operator import xor


def parse_data_int(puzzle_input: str) -> list[int]:
    return [int(n) for n in puzzle_input.split(",") if n != ""]


def parse_data_ascii(puzzle_input: str) -> list[int]:
    return [ord(n) for n in puzzle_input.strip()] + [
        17,
        31,
        73,
        47,
        23,
    ]


def knot_lst(lst: list[int], pos: int, lenght: int) -> list[int]:
    idxs = [(pos + l) % len(lst) for l in range(lenght)]
    vals = reversed([lst[i] for i in idxs])

    for i, v in zip(idxs, vals):
        lst[i] = v
    return lst


def knot_hash(end: int, knots: list[int], rounds=1) -> list[int]:
    lst = [n for n in range(0, end + 1)]
    idx = 0
    skip_size = 0
    for _ in range(rounds):
        for k in knots:
            lst = knot_lst(lst, idx, k)
            idx += k + skip_size
            skip_size += 1

    return lst


def densening_hash(lst: list[int]) -> list[int]:
    dense = []
    for n in range(int(len(lst) / 16)):
        dense.append(reduce(xor, lst[n * 16 : (n + 1) * 16]))
    return dense


def convert_to_hex(lst: int) -> str:
    return "".join([f"{d:02x}" for d in lst])


def solution_1(puzzle_input: str):
    data = parse_data_int(puzzle_input)
    hashed = knot_hash(255, data)
    return hashed[0] * hashed[1]


def solution_2(puzzle_input: str):
    data = parse_data_ascii(puzzle_input)
    hashed = knot_hash(255, data, rounds=64)
    hashed = densening_hash(hashed)
    return "".join([f"{d:02x}" for d in hashed])

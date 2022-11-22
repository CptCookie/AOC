from functools import reduce
from operator import xor


def parse_data_int(puzzle_input: str) -> list[int]:
    return [int(n) for n in puzzle_input.split(",") if n != ""]

def parse_data_byte(puzzle_input: str) -> list[int]:
    return [ord(n) for n in puzzle_input]



def knot_lst(lst: list[int], pos: int, lenght: int) -> list[int]:
    if lenght == 1:
        return lst

    if pos + lenght > len(lst):

        start_len = (pos + lenght) % len(lst)
        sub_lst = lst[pos:] + lst[: (pos + lenght) % len(lst)]
        i_sub_lst = sub_lst[::-1]
        return (
            i_sub_lst[-start_len:]
            + lst[start_len:pos]
            + i_sub_lst[: lenght - start_len]
        )
    else:
        i_sub_lst = lst[pos : pos + lenght][::-1]
        return lst[:pos] + i_sub_lst + lst[pos + lenght:]

def sparse_to_dense_hash(lst: list[int])-> list[int]:
    dense = []
    for n in range(1, 17):
        dense.append(reduce(xor, lst[n-1::16]))
    return dense


def knot_hash(end: int, knots: list[int], rounds=1) -> list[int]:
    lst = [n for n , _ in enumerate(range(0,end+1))]
    idx = 0
    skip_size = 0

    for k in knots:
        print(lst, idx, k, skip_size)
        lst = knot_lst(lst, idx, k)
        idx = (idx + k + skip_size) % len(lst)
        skip_size += 1

    return lst



def solution_1(puzzle_input: str):
    data = parse_data_int(puzzle_input)
    hashed = knot_hash(255, data)
    return hashed[0] * hashed[1]


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    return None

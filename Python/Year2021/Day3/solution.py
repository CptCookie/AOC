from typing import List


def get_common_bits(bit_list: List[str], most_common=True) -> str:
    common = ""
    for i in range(len(bit_list[0])):
        bits = [n[i] for n in bit_list]
        if bits.count("0") > len(bits) / 2:
            common += "0" if most_common else "1"
        else:
            common += "1" if most_common else "0"
    return common


def reduce_bitlist(bit_list, most_common_bit=True) -> str:
    for index in range(len(bit_list[0])):
        common = get_common_bits(bit_list, most_common_bit)
        bit_list = [bits for bits in bit_list if bits[index] == common[index]]

        if len(bit_list) == 1:
            return bit_list[0]
    return bit_list[0]


def solution_1(puzzle_input: str):
    puzzle_data = [n for n in puzzle_input.splitlines() if n != ""]
    return int(get_common_bits(puzzle_data), 2) * int(
        get_common_bits(puzzle_data, most_common=False), 2
    )


def solution_2(puzzle_input: str):
    puzzle_data = [n for n in puzzle_input.splitlines() if n != ""]
    return int(reduce_bitlist(puzzle_data), 2) * int(
        reduce_bitlist(puzzle_data, most_common_bit=False), 2
    )

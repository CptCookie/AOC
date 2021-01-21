from math import sqrt


def get_lowest_house(presents):
    house_presents = [0] * (int(presents / 10) + 1)

    for elf in range(1, int(presents / 10) + 1):
        for house in range(elf, int(presents / 10) + 1, elf):
            house_presents[house] += elf * 10
    for n, elem in enumerate(house_presents):
        if elem >= presents:
            return n


def get_lowest_house_limited(presents):
    house_presents = [0] * (int(presents / 10) + 1)

    for elf in range(1, int(presents / 10) + 1):
        for house in range(elf, min(int(presents / 10) + 1, elf * 50 + 1), elf):
            house_presents[house] += elf * 11
    for n, elem in enumerate(house_presents):
        if elem >= presents:
            return n


def solve(puzzle_input):
    print(puzzle_input)
    print(f"solution 1: {get_lowest_house(int(puzzle_input))}")
    print(f"solution 2: {get_lowest_house_limited(int(puzzle_input))}")

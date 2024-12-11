from collections import defaultdict
from math import floor, log10


def parse_input(aoc_input: str) -> dict[int, int]:
    stones = defaultdict(int)
    for n in aoc_input.split():
        if n.isnumeric():
            stones[int(n)] += 1
    return stones


def get_new_stones(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    digits = floor(log10(stone)) + 1
    if digits % 2 == 0:
        left, right = divmod(stone, 10 ** (digits // 2))
        return [left, right]

    else:
        return [stone * 2024]


def blink(stones: dict[int, int], n=1) -> dict[int, int]:
    for _ in range(n):
        new_stones = defaultdict(int)
        for num, count in stones.items():
            for new_num in get_new_stones(num):
                new_stones[new_num] += count
        stones = new_stones
    return stones


def solution_1(aoc_input: str):
    stones = parse_input(aoc_input)
    stones = blink(stones, 25)
    return sum(stones.values())


def solution_2(aoc_input: str):
    stones = parse_input(aoc_input)
    stones = blink(stones, 75)
    return sum(stones.values())

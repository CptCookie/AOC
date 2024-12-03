import re


def solution_1(aoc_input: str) -> int:
    matches = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", aoc_input)
    numbers = [map(int, m.groups()) for m in matches]
    return sum(a * b for a, b in numbers)


def solution_2(aoc_input: str) -> int:
    matches = re.finditer(r"mul\(([\d]{1,3}),([\d]{1,3})\)|don't\(\)|do\(\)", aoc_input)
    count = 0
    do = True

    for m in matches:
        if m.group() == "don't()":
            do = False
        if m.group() == "do()":
            do = True
        elif do:
            count += sum(map(int, m.groups()))
    return count

import requests
from const import token
import itertools


def get_aoc_input():
    r = requests.get(
        "https://adventofcode.com/2020/day/9/input", cookies={"session": token}
    )
    return [int(n) for n in r.content.decode().split("\n") if n != ""]


def is_combination_of(number, combinable):
    combinations = [sum(n) for n in list(itertools.combinations(combinable, 2))]
    return number in combinations


def search_invalid(sequenz, sequenz_length=25):
    for n, elem in enumerate(sequenz[sequenz_length:]):
        if not is_combination_of(elem, sequenz[n : sequenz_length + n + 1]):
            return elem


def find_continues_sum(number, sequenz):
    for n in range(len(sequenz)):
        if sum(sequenz[: n + 1]) == number:
            return sequenz[: n + 1]
        elif sum(sequenz[: n + 1]) > number:
            return []


def find_enryption_weakness(number, sequenz):
    for n in range(len(sequenz)):
        combination = find_continues_sum(number, sequenz[n:])
        if len(combination) > 0:
            return combination


def solve(puzzle_input):
    sequenz = [int(n) for n in puzzle_input.split("\n") if n != ""]
    fail_number = search_invalid(sequenz)
    print(f"solution 1: {fail_number}")

    encrypt_weakness = find_enryption_weakness(fail_number, sequenz)
    print(f"solution 2: {min(encrypt_weakness) + max(encrypt_weakness)}")

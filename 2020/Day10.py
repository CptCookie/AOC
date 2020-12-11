import requests
from const import token 
from itertools import chain, combinations

def get_aoc_input():
    r = requests.get("https://adventofcode.com/2020/day/10/input", cookies={"session": token})
    return [int(n) for n in r.content.decode().split('\n') if n != '']


def get_differnces(adapters: [int]):
    dif = [0,0,0]
    for n, elem in enumerate(adapters[1:]):
        dif[elem - adapters[n] - 1] += 1
    return dif

def number_valid_combinations(adapters):
    counter = 0
    combinations = 1
    combos = {0: 1, 1: 1, 2:2, 3:4, 4:7}
    for n, adapt in enumerate(adapters[1:]):
        if adapt - adapters[n] == 1:
            counter += 1
        else: # ccccombo bracker
            combinations *= combos[counter]
            counter = 0
    return combinations


def test_differences_1():
    data = sorted([ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4, 0, 22])
    assert get_differnces(data) == [7, 0, 5]

def test_differences_2():
    data = sorted([ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3, 0, 52])
    assert get_differnces(data) == [22, 0, 10]

def test_combinations():
    data = sorted([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])
    assert number_valid_combinations(data) == 8

if __name__ == "__main__":
    adapters = sorted(get_aoc_input())
    dif = get_differnces([0] + adapters + [max(adapters)+3])
    print(f'differences: {dif} -> solution 1: {dif[0] * dif[2]}')
    print(f'number of valid combinations: {number_valid_combinations([0] + adapters + [max(adapters)+3])}')
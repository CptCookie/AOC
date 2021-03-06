import re
import json


def find_numbers(search):
    regex = re.compile(r"-?\d+")
    return [int(n) for n in regex.findall(search)]


def find_without_red(search):
    red = re.compile(r'{.+"red".+}')
    for n in red.findall(search):
        search = search.replace(n, "")
    return find_numbers(search)


def sum_red(obj):
    if type(obj) == dict:
        if "red" in obj.values():
            return 0
        return sum([sum_red(n) for n in obj.values()])
    if type(obj) == list:
        return sum([sum_red(n) for n in obj])
    if type(obj) == int:
        return obj
    return 0


def solution_1(puzzle_input):
    puzzle_input = puzzle_input
    return sum(find_numbers(puzzle_input))


def solution_2(puzzle_input):
    puzzle_input = puzzle_input
    return sum_red(json.loads(puzzle_input))

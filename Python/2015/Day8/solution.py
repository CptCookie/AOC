import re

reghex = re.compile(r"\\x[0-9a-f]{2}")


def count_code(line: str):
    return len(line)


def count_char(line: str):
    line = line.replace(r"\\", "1")
    line = line.replace(r"\"", "2")
    for n in reghex.findall(line):
        line = line.replace(n, "0")
    return len(f"{line[1:-1]}")


def count_reencode(line: str):
    qoutes = line.count('"')
    slashes = line.count("\\")
    return len(line) + qoutes + slashes + 2


def solution_1(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    sum_code = sum([count_code(n) for n in puzzle_input])
    sum_char = sum([count_char(n) for n in puzzle_input])
    return sum_code - sum_char


def solution_2(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    sum_code = sum([count_code(n) for n in puzzle_input])
    sum_reencode = sum([count_reencode(n) for n in puzzle_input])
    return sum_reencode - sum_code

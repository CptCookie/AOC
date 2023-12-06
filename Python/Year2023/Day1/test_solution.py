from .solution import solution_1, solution_2, find_number, parse_input

TEST_INPUT = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

TEST_DATA = [
    "219",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_find_num():
    assert find_number("two1nine") == 29
    assert find_number("eightwothree") == 83
    assert find_number("abcone2threexyz") == 13
    assert find_number("xtwone3four") == 24
    assert find_number("4nineeightseven2") == 42
    assert find_number("zoneight234") == 14
    assert find_number("7pqrstsixteen") == 76


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT)

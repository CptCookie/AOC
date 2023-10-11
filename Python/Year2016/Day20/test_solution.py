from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """5-8
0-2
4-7
"""

TEST_DATA = [(5, 8), (0, 2), (4, 7)]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 3


def test_solution_2():
    assert solution_2(TEST_INPUT, max_num=9) == 2

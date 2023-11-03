from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

TEST_DATA = []


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 4


def test_solution_2():
    assert solution_2(TEST_INPUT) == {2}

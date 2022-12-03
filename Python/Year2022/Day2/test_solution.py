from .solution import solution_1, solution_2

TEST_DATA = """A Y
B X
C Z"""


def test_solution_1():
    assert solution_1(TEST_DATA) == 15


def test_solution_2():
    assert solution_2(TEST_DATA) == 12

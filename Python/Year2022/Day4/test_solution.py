from .solution import solution_1, solution_2

TEST_DATA = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_solution_1():
    assert solution_1(TEST_DATA) == 2


def test_solution_2():
    assert solution_2(TEST_DATA) == 4

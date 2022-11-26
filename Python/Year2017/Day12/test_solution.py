from .solution import solution_1, solution_2

TEST_DATA = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5
"""


def test_solution_1():
    assert solution_1(TEST_DATA) == 6


def test_solution_2():
    assert solution_2(TEST_DATA) == 2

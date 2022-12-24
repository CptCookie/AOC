from .solution import solution_1, solution_2

TEST_INPUT = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
"""


def test_solution_1():
    assert solution_1(TEST_INPUT) == 64


def test_solution_2():
    assert solution_2(TEST_INPUT) == 58

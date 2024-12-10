from .solution import solution_1, solution_2

TEST_INPUT = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""


def test_solution_1():
    assert solution_1(TEST_INPUT) == 36


def test_solution_2():
    assert solution_2(TEST_INPUT) == 81

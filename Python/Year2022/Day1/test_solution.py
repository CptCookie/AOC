from .solution import solution_1, solution_2

EXAMPLE = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def test_solution_1():
    assert solution_1(EXAMPLE) == 24000


def test_solution_2():
    assert solution_2(EXAMPLE) == 45000

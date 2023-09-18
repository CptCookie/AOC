from .solution import solution_1, solution_2
EXAMPLE = "dabAcCaCBAcCcaDA\n"


def test_sol_1():
    assert solution_1(EXAMPLE) == 10


def test_sol_2():
    assert solution_2(EXAMPLE) == 4

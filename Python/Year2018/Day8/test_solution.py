from .solution import solution_1, solution_2


EXAMPLE = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"


def test_sol_1():
    assert solution_1(EXAMPLE) == 138


def test_sol_2():
    assert solution_2(EXAMPLE) == 66

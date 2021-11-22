from .solution import solution_1, solution_2

test_input = "1\n2\n3\n4\n5\n7\n8\n9\n10\n11\n"


def test_solution_1():
    assert solution_1(test_input) == 99


def test_solution_2():
    assert solution_2(test_input) == 44

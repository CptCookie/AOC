from .solution import solution_1, solution_2, n_septs_to_leave


def test_n_steps():
    assert n_septs_to_leave([0, 3, 0, 1, -3], lambda x: 1) == 5


def test_solution_1():
    test_input = "0\n3\n0\n1\n-3"
    assert solution_1(test_input) == 5


def test_solution_2():
    test_input = "0\n3\n0\n1\n-3"
    assert solution_2(test_input) == 10

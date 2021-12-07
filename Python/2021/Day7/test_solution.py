from .solution import solution_1, solution_2


def test_solution_1():
    test_input = "16,1,2,0,4,2,7,1,2,14"
    assert solution_1(test_input) == 37


def test_solution_2():
    test_input = "16,1,2,0,4,2,7,1,2,14"
    assert solution_2(test_input) == 168

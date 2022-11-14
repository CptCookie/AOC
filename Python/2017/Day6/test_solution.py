from .solution import solution_1, solution_2, redistribute_memory


def test_redistribute_memory():
    assert redistribute_memory([4, 0, 0, 0]) == [1, 1, 1, 1]
    assert redistribute_memory([0, 0, 3, 0]) == [1, 1, 0, 1]
    assert redistribute_memory([1, 2, 3, 4]) == [2, 3, 4, 1]


def test_solution_1():
    test_input = "0\t2\t7\t0"
    assert solution_1(test_input) == 5


def test_solution_2():
    test_input = "0\t2\t7\t0"
    assert solution_2(test_input) == 4

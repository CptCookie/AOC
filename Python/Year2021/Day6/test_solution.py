from .solution import solution_1, solution_2, simulate_day, parse_lanternfish


def test_simulate_day():
    assert simulate_day([0, 0, 1, 0, 0, 0, 0, 0, 0]) == [0, 1, 0, 0, 0, 0, 0, 0, 0]


def test_simulate_reproduction():
    assert simulate_day([1, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0, 1, 0, 1]


def test_parse():
    assert parse_lanternfish("3,4,3,1,2") == [0, 1, 1, 2, 1, 0, 0, 0, 0]


def test_solution_1():
    test_input = "3,4,3,1,2"
    assert solution_1(test_input) == 5934


def test_solution_2():
    test_input = "3,4,3,1,2"
    assert solution_2(test_input) == 26984457539

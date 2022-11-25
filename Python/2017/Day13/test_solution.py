from .solution import solution_1, solution_2, parse_data

TEST_DATA = """0: 3
1: 2
4: 4
6: 4"""


def test_parse_data():
    assert parse_data(TEST_DATA) == {0: 3, 1: 2, 4: 4, 6: 4}


def test_solution_1():
    assert solution_1(TEST_DATA) == 24


def test_solution_2():
    assert solution_2(TEST_DATA) == 10

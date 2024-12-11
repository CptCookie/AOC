from .solution import solution_1, parse_input, get_new_stones

TEST_INPUT = """125 17
"""

TEST_DATA = {125: 1, 17: 1}


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_get_new_stones():
    assert get_new_stones(0) == [1]
    assert get_new_stones(1) == [2024]
    assert get_new_stones(10) == [1, 0]
    assert get_new_stones(99) == [9, 9]
    assert get_new_stones(999) == [2021976]


def test_solution_1():
    assert solution_1(TEST_INPUT) == 55312

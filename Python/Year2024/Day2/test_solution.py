from .solution import solution_1, solution_2, parse_input, is_safe

TEST_INPUT = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

TEST_DATA = [
    [7, 6, 4, 2, 1],
    [1, 2, 7, 8, 9],
    [9, 7, 6, 2, 1],
    [1, 3, 2, 4, 5],
    [8, 6, 4, 4, 1],
    [1, 3, 6, 7, 9],
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_is_safe():
    assert is_safe(TEST_DATA[0])
    assert not is_safe(TEST_DATA[1])
    assert not is_safe(TEST_DATA[2])
    assert not is_safe(TEST_DATA[3])
    assert not is_safe(TEST_DATA[4])
    assert is_safe(TEST_DATA[5])


def test_is_dampened_safe():
    assert is_safe(TEST_DATA[0], True)
    assert not is_safe(TEST_DATA[1], True)
    assert not is_safe(TEST_DATA[2], True)
    assert is_safe(TEST_DATA[3], True)
    assert is_safe(TEST_DATA[4], True)
    assert is_safe(TEST_DATA[5], True)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 2


def test_solution_2():
    assert solution_2(TEST_INPUT) == 4

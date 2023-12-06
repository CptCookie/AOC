from .solution import solution_1, solution_2, parse_input, number_close_pos

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def test_solution_1():
    assert solution_1(TEST_INPUT) == 4361


def test_close_1():
    number_start = (2, 2)
    number = 3

    for test_pos in (
        (1, 1),
        (2, 1),
        (3, 1),
        (3, 2),
        (3, 3),
        (2, 3),
        (1, 3),
        (1, 2),
    ):
        assert number_close_pos(number_start, number, test_pos)


def test_close_2():
    number_start = (2, 2)
    number = 34

    for test_pos in (
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (4, 2),
        (4, 3),
        (3, 3),
        (2, 3),
        (1, 3),
        (1, 2),
    ):
        assert number_close_pos(number_start, number, test_pos)


def test_close_3():
    number_start = (2, 2)
    number = 345

    for test_pos in (
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (5, 1),
        (5, 2),
        (5, 3),
        (4, 3),
        (3, 3),
        (2, 3),
        (1, 3),
        (1, 2),
    ):
        assert number_close_pos(number_start, number, test_pos)


def test_solution_2():
    assert solution_2(TEST_INPUT)

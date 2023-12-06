from .solution import solution_1, solution_2, parse_input, number_close_pos

TEST_INPUT = """467..114..
...*......
..35..633.
......#...
617*......
.....+.581
..592.....
......755.
...$.*....
.664.598..
"""

TEST_NUMBERS = [
    (467, (0, 0)),
    (114, (5, 0)),
    (35, (2, 2)),
    (633, (6, 2)),
    (617, (0, 4)),
    (581, (7, 5)),
    (592, (2, 6)),
    (755, (6, 7)),
    (664, (1, 9)),
    (598, (5, 9)),
]

TEST_SYMBOLS = [
    ("*", (3, 1)),
    ("#", (6, 3)),
    ("*", (3, 4)),
    ("+", (5, 5)),
    ("$", (3, 8)),
    ("*", (5, 8)),
]


def test_parse():
    assert parse_input(TEST_INPUT) == (TEST_NUMBERS, TEST_SYMBOLS)


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
    assert solution_2(TEST_INPUT) == 467835

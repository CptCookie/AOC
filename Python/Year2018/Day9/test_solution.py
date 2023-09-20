from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """9 players; last marble is worth 25 points
"""

TEST_DATA = (9, 25)


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 32
    assert solution_1("10 players; last marble is worth 1618 points") == 8317
    assert solution_1("13 players; last marble is worth 7999 points") == 146373
    assert solution_1("17 players; last marble is worth 1104 points") == 2764
    assert solution_1("21 players; last marble is worth 6111 points") == 54718
    assert solution_1("30 players; last marble is worth 5807 points") == 37305


def test_solution_2():
    assert solution_2(TEST_INPUT)

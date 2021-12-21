from .solution import *

TEST_DATA = """Player 1 starting position: 4
Player 2 starting position: 8"""


def test_play():
    assert play(4, 8) == ([1000, 745], 331)


def test_parse():
    assert parse_data(TEST_DATA) == [4, 8]


def test_solution_1():
    assert solution_1(TEST_DATA) == 739785


def test_solution_2():
    assert solution_2(TEST_DATA) == 444356092776315

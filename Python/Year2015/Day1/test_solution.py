from .solution import *


def test_parser():
    assert parse_stairs("((()") == [UP, UP, UP, DOWN]


def test_last_floor():
    assert last_floor([UP, UP, UP, DOWN]) == 2


def test_find_floor():
    assert find_floor([UP, UP, UP, DOWN], 3) == 2

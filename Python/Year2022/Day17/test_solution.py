from .solution import solution_1, solution_2, parse_input, Tetris
from utils.tests import assertSublist

TEST_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

TEST_DATA = []


def test_play():
    field = Tetris([n for n in TEST_INPUT])
    field.play_stone()
    assert field.rested_piece == [(2, 0), (3, 0), (4, 0), (5, 0)]


def test_play_double():
    field = Tetris([n for n in TEST_INPUT])
    field.play_stone()
    field.play_stone()
    assertSublist(field.rested_piece, [(3, 1), (2, 2), (3, 2), (4, 2), (3, 3)])


# def test_parsing():
#     assert parse_input(TEST_INPUT) == TEST_DATA


# def test_solution_1():
#     assert solution_1(TEST_INPUT)


# def test_solution_2():
#     assert solution_2(TEST_INPUT)

from .solution import solution_1, solution_2, Tetris
from utils.tests import assertSublist

TEST_INPUT = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

TEST_DATA = []


def test_play_stone_1():
    field = Tetris([n for n in TEST_INPUT])
    field.play_stones(1)
    assertSublist(field.rested_piece, [(2, 0), (3, 0), (4, 0), (5, 0)])
    assert field.current_height == 1


def test_play_stone_2():
    field = Tetris([n for n in TEST_INPUT])
    field.play_stones(2)
    assertSublist(field.rested_piece, [(2, 2), (3, 2),(4,2), (3, 3), (3, 1)])
    assert field.current_height == 4



def test_play_stone_3():
    field = Tetris([n for n in TEST_INPUT])
    field.play_stones(3)
    assertSublist(field.rested_piece, [(0, 3), (1, 3), (2, 3), (2, 4), (2, 5)])
    assert field.current_height == 6


def test_play_stone_4():
    field = Tetris([n for n in TEST_INPUT])
    field.play_stones(4)
    assertSublist(field.rested_piece, [(4, 3), (4, 4), (4, 5), (4, 6)])
    assert field.current_height == 7


def test_solution_1():
    assert solution_1(TEST_INPUT) == 3068


def test_solution_2():
    assert solution_2(TEST_INPUT) ==

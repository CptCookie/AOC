from .solution import *

TEST_INPUT = "target area: x=20..30, y=-10..-5"
TEST_AREA_X = (20, 30)
TEST_AREA_Y = (-10, -5)


def test_calc_pos():
    assert calc_pos(5, 1) == 5
    assert calc_pos(5, 2) == 9
    assert calc_pos(5, 3) == 12
    assert calc_pos(5, 4) == 14
    assert calc_pos(5, 5) == 15
    assert calc_pos(5, 6) == 15
    assert calc_pos(5, 7) == 14
    assert calc_pos(5, 8) == 12
    assert calc_pos(5, 9) == 9
    assert calc_pos(5, 10) == 5
    assert calc_pos(5, 11) == 0
    assert calc_pos(5, 12) == -6


def test_passes_area():
    assert dimension_passes_area(2, -5, -10) == [7]
    assert dimension_passes_area(3, -5, -10) == [9]
    assert dimension_passes_area(9, -5, -10) == [20]
    assert dimension_passes_area(0, -5, -10) == [4, 5]
    assert dimension_passes_area(0, -1, -10) == [2, 3, 4, 5]
    assert dimension_passes_area(-4, -5, -10) == [2]

    assert dimension_passes_area(10, -5, -10) == []


def test_iterate():
    assert iterate_throw([7, 2], TEST_AREA_X, TEST_AREA_Y)
    assert iterate_throw([6, 3], TEST_AREA_X, TEST_AREA_Y)
    assert iterate_throw([9, 0], TEST_AREA_X, TEST_AREA_Y)
    assert not iterate_throw([17, -4], TEST_AREA_X, TEST_AREA_Y)


def test_sol_2():
    assert solution_2(TEST_INPUT) == 112

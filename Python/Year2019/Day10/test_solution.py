import math

from .solution import (
    solution_1,
    solution_2,
    parse_input,
    get_num_visible,
    get_first_vaporized,
    astroid_rad_north_normal,
)

TEST_INPUT = """.#..#
.....
#####
....#
...##
"""

TEST_DATA = [
    (1, 0),
    (4, 0),
    (0, 2),
    (1, 2),
    (2, 2),
    (3, 2),
    (4, 2),
    (4, 3),
    (3, 4),
    (4, 4),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_get_num_visible():
    assert get_num_visible(TEST_DATA, (1, 0)) == 7
    assert get_num_visible(TEST_DATA, (3, 4)) == 8


def test_rad():
    assert astroid_rad_north_normal((3, 3), (3, 2)) / math.pi == 0
    assert astroid_rad_north_normal((3, 3), (4, 2)) / math.pi == 1 / 4
    assert astroid_rad_north_normal((3, 3), (4, 3)) / math.pi == 1 / 2
    assert astroid_rad_north_normal((3, 3), (4, 4)) / math.pi == 3 / 4
    assert astroid_rad_north_normal((3, 3), (3, 4)) / math.pi == 1
    assert astroid_rad_north_normal((3, 3), (2, 4)) / math.pi == 5 / 4
    assert astroid_rad_north_normal((3, 3), (2, 3)) / math.pi == 3 / 2
    assert astroid_rad_north_normal((3, 3), (2, 2)) / math.pi == 7 / 4


def test_vaporizer():
    astoroids = parse_input(
        """.#....#####...#..\n##...##.#####..##\n##...#...#.#####.\n..#.....X...###..\n..#.#.....#....##"""
    )
    vaporized = get_first_vaporized(astoroids, (8, 3))
    assert vaporized == [
        (8, 1),
        (9, 0),
        (9, 1),
        (10, 0),
        (9, 2),
        (11, 1),
        (12, 1),
        (11, 2),
        (15, 1),
        (12, 2),
        (13, 2),
        (14, 2),
        (15, 2),
        (12, 3),
        (16, 4),
        (15, 4),
        (10, 4),
        (4, 4),
        (2, 4),
        (2, 3),
        (0, 2),
        (1, 2),
        (0, 1),
        (1, 1),
        (5, 2),
        (1, 0),
        (5, 1),
        (6, 1),
        (6, 0),
        (7, 0),
    ]


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT)

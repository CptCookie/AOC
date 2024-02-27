from .solution import solution_1, solution_2, parse_rocks, tilt_dish, NORTH

TEST_INPUT = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

TEST_LOOSE = [
    (0, 0),
    (0, 1),
    (2, 1),
    (3, 1),
    (0, 3),
    (1, 3),
    (4, 3),
    (9, 3),
    (1, 4),
    (7, 4),
    (0, 5),
    (5, 5),
    (2, 6),
    (6, 6),
    (9, 6),
    (7, 7),
    (1, 9),
    (2, 9),
]


NORTH_MOVE = """OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#...."""


def test_parse_loose():
    _, loose = parse_rocks(TEST_INPUT)
    for p in TEST_LOOSE:
        assert p in loose


def test_tilt_north():
    rocks = parse_rocks(TEST_INPUT)
    loose_rocks = tilt_dish(*rocks, NORTH)

    _, expected_loose = parse_rocks(NORTH_MOVE)
    assert loose_rocks == expected_loose


def test_solution_1():
    assert solution_1(TEST_INPUT) == 136


def test_solution_2():
    assert solution_2(TEST_INPUT) == 64

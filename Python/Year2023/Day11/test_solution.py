from .solution import (
    solution_1,
    solution_2,
    parse_input,
    expand_universe,
    get_empty_rows,
    get_empty_cols,
    distance,
)

TEST_INPUT = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

TEST_DATA = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]


TEST_EXPANDED = [
    "....#........",
    ".........#...",
    "#............",
    ".............",
    ".............",
    "........#....",
    ".#...........",
    "............#",
    ".............",
    ".............",
    ".........#...",
    "#....#.......",
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_expanded():
    assert expand_universe(TEST_DATA) == TEST_EXPANDED


def test_empty_rows():
    assert get_empty_rows(TEST_DATA) == {3, 7}


def test_empty_col():
    assert get_empty_cols(TEST_DATA) == {2, 5, 8}


def test_distance():
    # test example 5 to 9
    assert distance((1, 6), (5, 11), [], [], 1) == 9
    assert distance((1, 6), (5, 11), [], [], 1) == 9
    assert distance((1, 5), (4, 9), [], [], 1) == 7
    assert distance((1, 5), (4, 9), [2, 8, 5], [3, 7], 2) == 9

    assert distance((4, 9), (1, 5), [], [], 1) == 7
    assert distance((4, 9), (1, 5), [2, 8, 5], [3, 7], 2) == 9
    assert distance((1, 5), (4, 9), [2, 8, 5], [3, 7], 10) == 25

    assert distance((0, 2), (9, 6), [], [], 1) == 13
    assert distance((0, 2), (9, 6), [2, 8, 5], [3, 7], 2) == 17
    assert distance((0, 2), (9, 6), [2, 8, 5], [3, 7], 10) == 49

    assert distance((0, 9), (4, 9), [], [], 1) == 4
    assert distance((0, 9), (4, 9), [2, 8, 5], [3, 7], 2) == 5
    assert distance((0, 9), (4, 9), [2, 8, 5], [3, 7], 10) == 13


def test_solution_1():
    assert solution_1(TEST_INPUT) == 374


def test_solution_2():
    assert solution_2("""#.#\n...\n..#""", 10) == 44
    assert solution_2(TEST_INPUT, 100) == 8410

from .solution import solution_1, solution_2, parse_input, is_looping

TEST_INPUT = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

TEST_MAP = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#........",
    "........#.",
    "#.........",
    "......#...",
]


TEST_POS = (4, 6)


def test_parsing():
    assert parse_input(TEST_INPUT) == (TEST_POS, TEST_MAP)


def test_looping():
    assert is_looping(TEST_POS, (3, 6), TEST_MAP)
    assert not is_looping(TEST_POS, (2, 6), TEST_MAP)
    assert not is_looping(TEST_POS, (0, 0), TEST_MAP)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 41


def test_solution_2():
    assert solution_2(TEST_INPUT) == 6

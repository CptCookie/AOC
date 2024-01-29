from .solution import solution_1, solution_2, parse_input, get_reflection

TEST_INPUT = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

TEST_DATA = [
    [
        "#.##..##.",
        "..#.##.#.",
        "##......#",
        "##......#",
        "..#.##.#.",
        "..##..##.",
        "#.#.##.#.",
    ],
    [
        "#...##..#",
        "#....#..#",
        "..##..###",
        "#####.##.",
        "#####.##.",
        "..##..###",
        "#....#..#",
    ],
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_reflection():
    assert get_reflection(TEST_DATA[0]) == 5


def test_solution_1():
    assert solution_1(TEST_INPUT) == 405


def test_solution_2():
    assert solution_2(TEST_INPUT) == 400

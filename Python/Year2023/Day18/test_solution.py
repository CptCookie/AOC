from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

TEST_DATA = [
    ("R", 6, "70c710"),
    ("D", 5, "0dc571"),
    ("L", 2, "5713f0"),
    ("D", 2, "d2c081"),
    ("R", 2, "59c680"),
    ("D", 2, "411b91"),
    ("L", 5, "8ceee2"),
    ("U", 2, "caa173"),
    ("L", 1, "1b58a2"),
    ("U", 2, "caa171"),
    ("R", 2, "7807d2"),
    ("U", 3, "a77fa3"),
    ("L", 2, "015232"),
    ("U", 2, "7a21e3"),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 62


def test_solution_2():
    assert solution_2(TEST_INPUT)

from .solution import (
    solution_1,
    solution_2,
    parse_simple,
    translate_vertices_to_pos,
    shoelace_surface,
)


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
    ("R", 6),
    ("D", 5),
    ("L", 2),
    ("D", 2),
    ("R", 2),
    ("D", 2),
    ("L", 5),
    ("U", 2),
    ("L", 1),
    ("U", 2),
    ("R", 2),
    ("U", 3),
    ("L", 2),
    ("U", 2),
]

TEST_POS = [
    (0, 0),
    (6, 0),
    (6, -5),
    (4, -5),
    (4, -7),
    (6, -7),
    (6, -9),
    (1, -9),
    (1, -7),
    (0, -7),
    (0, -5),
    (2, -5),
    (2, -2),
    (0, -2),
    (0, 0),
]


def test_parsing():
    assert parse_simple(TEST_INPUT) == TEST_DATA


def test_translation():
    assert translate_vertices_to_pos(TEST_DATA) == TEST_POS


def test_shoelace():
    assert (shoelace_surface([(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)])) == 1
    assert (shoelace_surface([(0, 0), (0, 2), (1, 2), (1, 0), (0, 0)])) == 2
    assert (
        shoelace_surface(
            [
                (0, -2),
                (6, -2),
                (9, -0.5),
                (6, 2),
                (9, 4.5),
                (4, 7),
                (-1, 6),
                (-3, 3),
                (0, -2),
            ]
        )
        == 77
    )


def test_solution_1():
    assert solution_1(TEST_INPUT) == 62


def test_solution_2():
    assert solution_2(TEST_INPUT) == 952408144115

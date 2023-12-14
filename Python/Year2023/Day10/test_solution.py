from .solution import (
    solution_1,
    solution_2,
    parse_input,
    get_start,
    first_step,
    N,
    E,
    S,
    W,
    get_loop,
)

TEST_INPUT = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""

TEST_DATA = ["7-F7-", ".FJ|7", "SJLL7", "|F--J", "LJ.LJ"]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_get_start():
    assert get_start(TEST_DATA) == (0, 2)


def test_first_step():
    step = first_step(TEST_DATA, (0, 2))

    assert step == ((1, 2), N) or step == ((0, 3), S)


def test_get_loop():
    test_data = [
        ".....",
        ".S-7.",
        ".|.|.",
        ".L-J.",
        ".....",
    ]
    loop = get_loop(test_data)
    expected = [(1, 1), (2, 1), (3, 1), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2)]
    for ex in expected:
        assert ex in loop


def test_loop_len():
    assert len(get_loop(TEST_DATA)) == 16


def test_solution_1():
    assert solution_1(TEST_INPUT) == 8


def test_solution_2_simple():
    test_data = """.....
.F-7.
.|.|.
.L-S.
....."""

    assert solution_2(test_data) == 1


def test_solution_2():
    test_data = """..........
.S-------7
.|F----7.|
.||OOOO|.|
.||OOOO|.|
.|L-7F-J.|
.|II||IIFJ
.L--JL--J.
.........."""

    assert solution_2(test_data) == 8


def test_solution_2_complexe():
    test_data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

    assert solution_2(test_data) == 10

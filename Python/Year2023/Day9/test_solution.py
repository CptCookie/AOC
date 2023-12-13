from .solution import (
    solution_1,
    solution_2,
    parse_input,
    build_diff_triangle,
    extrapolate_next_value,
    extrapolate_prev_value,
)

TEST_INPUT = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

TEST_DATA = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45],
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_triangle():
    assert build_diff_triangle([0, 3, 6, 9, 12, 15]) == [
        [0, 3, 6, 9, 12, 15],
        [3, 3, 3, 3, 3],
    ]

    assert build_diff_triangle([10, 13, 16, 21, 30, 45]) == [
        [10, 13, 16, 21, 30, 45],
        [3, 3, 5, 9, 15],
        [0, 2, 4, 6],
        [2, 2, 2],
    ]


def test_next_value():
    assert extrapolate_next_value([0, 3, 6, 9, 12, 15]) == 18
    assert extrapolate_next_value([1, 3, 6, 10, 15, 21]) == 28
    assert extrapolate_next_value([10, 13, 16, 21, 30, 45]) == 68


def test_prev_value():
    assert extrapolate_prev_value([0, 3, 6, 9, 12, 15]) == -3
    assert extrapolate_prev_value([1, 3, 6, 10, 15, 21]) == 0
    assert extrapolate_prev_value([10, 13, 16, 21, 30, 45]) == 5


def test_solution_1():
    assert solution_1(TEST_INPUT) == 114


def test_solution_2():
    assert solution_2(TEST_INPUT)

from .solution import (
    solution_1,
    solution_2,
    get_sightlines,
    parse_data,
    is_tree_visible,
    get_sceenic_value,
)

TEST_INPUT = """30373
25512
65332
33549
35390"""


TEST_DATA = [
    [3, 0, 3, 7, 3],
    [2, 5, 5, 1, 2],
    [6, 5, 3, 3, 2],
    [3, 3, 5, 4, 9],
    [3, 5, 3, 9, 0],
]


def test_parse():
    assert parse_data(TEST_INPUT) == TEST_DATA


def test_sightline():
    get_sightlines(TEST_DATA, (0, 0)) == [[], [0, 3, 7, 3], [], [2, 6, 3, 3]]
    get_sightlines(TEST_DATA, (4, 4)) == [[9, 3, 5, 3], [], [9, 2, 2, 3], []]
    get_sightlines(TEST_DATA, (2, 3)) == [[3], [5, 4, 9], [5, 5, 0], [5]]


def test_sceenic_value():
    assert get_sceenic_value(3, [[], []]) == 0
    assert get_sceenic_value(3, [[2, 3], []]) == 0
    assert get_sceenic_value(3, [[5], [6]]) == 1
    assert get_sceenic_value(3, [[2, 3], [6]]) == 2
    assert get_sceenic_value(5, [[5, 2], [3], [1, 2], [3, 5, 3]]) == 4
    assert get_sceenic_value(5, [[3, 3], [4, 9], [3], [3, 5, 3]]) == 8


def test_visible():
    assert is_tree_visible(3, [[], [5, 6]])
    assert not is_tree_visible(3, [[3, 4, 5], [2, 3, 4]])
    assert is_tree_visible(5, [[2, 3], [5, 6]])


def test_solution_1():
    assert solution_1(TEST_INPUT) == 21


def test_solution_2():
    assert solution_2(TEST_INPUT) == 8

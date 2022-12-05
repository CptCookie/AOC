from copy import deepcopy
from .solution import parse_data, solution_1, solution_2, move_crates


TEST_INPUT = """[V]     [B]                     [C]
[C]     [N] [G]         [W]     [P]
[W]     [C] [Q] [S]     [C]     [M]
[L]     [W] [B] [Z]     [F] [S] [V]
[R]     [G] [H] [F] [P] [V] [M] [T]
[M] [L] [R] [D] [L] [N] [P] [D] [W]
[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
 1   2   3   4   5   6   7   8   9 

move 1 from 9 to 2
move 23 from 6 to 1
move 4 from 2 to 3
move 11 from 8 to 7
move 4 from 1 to 2"""

test_satck = [
    ["Z", "N"],
    ["M", "C", "D"],
    [
        "P",
    ],
]

test_moves = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]


def test_move_crate():
    assert move_crates(test_satck, 1, 2, 1, True) == [["Z", "N", "D"], ["M", "C"], ["P"]]
    assert move_crates([["Z", "N", "D"], ["M", "C"], ["P"]], 3, 1, 3, True) == [
        [],
        ["M", "C"],
        ["P", "D", "N", "Z"],
    ]
    assert move_crates([[], ["M", "C"], ["P", "D", "N", "Z"]], 2, 2, 1, True) == [
        ["C", "M"],
        [],
        ["P", "D", "N", "Z"],
    ]
    assert move_crates([["C", "M"], [], ["P", "D", "N", "Z"]], 1, 1, 2, True) == [
        ["C"],
        ["M"],
        ["P", "D", "N", "Z"],
    ]


def test_move_create_end():
    assert move_crates([[], ["a", "b", "c"]], 1, 2, 1, True) == [["c"], ["a", "b"]]
    assert move_crates([[], ["a", "b", "c"]], 2, 2, 1, True) == [["c", "b"], ["a"]]
    assert move_crates([[], ["a", "b", "c"]], 3, 2, 1, True) == [["c", "b", "a"], []]

def test_move_all_crates():
    assert move_crates([[], ["a", "b", "c"]], 1, 2, 1) == [["c"], ["a", "b"]]
    assert move_crates([[], ["a", "b", "c"]], 2, 2, 1) == [["b", "c"], ["a"]]
    assert move_crates([[], ["a", "b", "c"]], 3, 2, 1) == [["a", "b", "c"], []]


def test_parse_stack():
    stack, _ = parse_data(TEST_INPUT)
    assert stack == [
        ["Q", "F", "M", "R", "L", "W", "C", "V"],
        ["D", "Q", "L"],
        ["P", "S", "R", "G", "W", "C", "N", "B"],
        ["L", "C", "D", "H", "B", "Q", "G"],
        ["V", "G", "L", "F", "Z", "S"],
        ["D", "G", "N", "P"],
        ["D", "Z", "P", "V", "F", "C", "W"],
        ["C", "P", "D", "M", "S"],
        ["Z", "N", "W", "T", "V", "M", "P", "C"],
    ]


def test_parse_moves():
    _, moves = parse_data(TEST_INPUT)
    assert moves == [[1, 9, 2], [23, 6, 1], [4, 2, 3], [11, 8, 7], [4, 1, 2]]

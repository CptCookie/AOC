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
move 4 from 6 to 1
move 4 from 2 to 6
move 5 from 8 to 7
move 4 from 9 to 2"""

test_satck = [
    ["Z", "N"],
    ["M", "C", "D"],
    [
        "P",
    ],
]

test_moves = [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]


def test_move_crate():
    assert move_crates(test_satck, 1, 2, 1) == [["Z", "N", "D"], ["M", "C"], ["P"]]
    assert move_crates([["Z", "N", "D"], ["M", "C"], ["P"]], 3, 1, 3) == [
        [],
        ["M", "C"],
        ["P", "D", "N", "Z"],
    ]
    assert move_crates([[], ["M", "C"], ["P", "D", "N", "Z"]], 2, 2, 1) == [
        ["C", "M"],
        [],
        ["P", "D", "N", "Z"],
    ]
    assert move_crates([["C", "M"], [], ["P", "D", "N", "Z"]], 1, 1, 2) == [
        ["C"],
        ["M"],
        ["P", "D", "N", "Z"],
    ]


def test_move_create_end():
    assert move_crates([[], ["a", "b", "c"]], 1, 2, 1) == [["c"], ["a", "b"]]
    assert move_crates([[], ["a", "b", "c"]], 2, 2, 1) == [["c", "b"], ["a"]]
    assert move_crates([[], ["a", "b", "c"]], 3, 2, 1) == [["c", "b", "a"], []]


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
    assert moves == [[1, 9, 2], [4, 6, 1], [4, 2, 6], [5, 8, 7], [4, 9, 2]]


def test_solution_1():
    stacks = deepcopy(test_satck)
    for m in test_moves:
        stacks = move_crates(stacks, *m)

    assert "".join([l[-1] for l in stacks]) == "CMZ"


# def test_solution_2():
#     pass

from .solution import *

TEST_DATA = """
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


def test_parse_points():
    assert parse_points("""6,10\n0,14\n9,10\n0,3\n10,4\n""") == [
        (6, 10),
        (0, 14),
        (9, 10),
        (0, 3),
        (10, 4),
    ]


def test_parse_instructions():
    assert parse_instuctions("fold along y=7\nfold along x=5\n") == [
        ("y", "7"),
        ("x", "5"),
    ]


def test_fold_x():
    og = [[True, False, False], [False, False, False], [False, False, True]]
    assert fold_x(og, 1) == [[True], [False], [True]]


def test_fold_x_off_center():
    og = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    expected = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1],
        [0, 0, 0],
    ]

    assert fold_x(og, 3) == expected


def test_fold_y():
    og = [[True, False, False], [False, False, False], [False, False, True]]
    assert fold_y(og, 1) == [[True, False, True]]


def test_fold_y_off_center():
    og = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ]

    expected = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
    ]

    fold_y(og, 3) == expected


def test_solution_1():
    assert solution_1(TEST_DATA) == 17


# def test_solution_2():
#     test_input = ""
#     assert False

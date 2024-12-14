from .solution import parse_input, safety_ratings, calculate_pos

TEST_INPUT = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3

"""

TEST_DATA = [
    (0, 4, 3, -3),
    (6, 3, -1, -3),
    (10, 3, -1, 2),
    (2, 0, 2, -1),
    (0, 0, 1, 3),
    (3, 0, -2, -2),
    (7, 6, -1, -3),
    (3, 0, -1, -2),
    (9, 3, 2, 3),
    (7, 3, -1, 2),
    (2, 4, 2, -3),
    (9, 5, -3, -3),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_calculate_pos():
    assert calculate_pos((2, 4, 2, -3), 11, 7, 1) == (4, 1)
    assert calculate_pos((2, 4, 2, -3), 11, 7, 2) == (6, 5)
    assert calculate_pos((2, 4, 2, -3), 11, 7, 3) == (8, 2)
    assert calculate_pos((2, 4, 2, -3), 11, 7, 4) == (10, 6)
    assert calculate_pos((2, 4, 2, -3), 11, 7, 5) == (1, 3)

    assert calculate_pos((2, 4, -2, 3), 11, 7, 1) == (0, 0)
    assert calculate_pos((2, 4, -2, 3), 11, 7, 2) == (9, 3)


def test_solution_1():
    assert safety_ratings(TEST_DATA, 11, 7, 100) == 12

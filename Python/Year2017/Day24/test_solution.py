from .solution import solution_1, solution_2, parse_input, get_next_bridges, strength

TEST_INPUT = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""

TEST_DATA = [
    (0, 2),
    (2, 2),
    (2, 3),
    (3, 4),
    (3, 5),
    (0, 1),
    (10, 1),
    (9, 10),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_next_bridges():
    assert get_next_bridges([(0, 0)], TEST_DATA) == [[(0, 0), (0, 2)], [(0, 0), (0, 1)]]
    assert get_next_bridges([(0, 0), (0, 2)], TEST_DATA) == [
        [(0, 0), (0, 2), (2, 2)],
        [(0, 0), (0, 2), (2, 3)],
    ]
    assert get_next_bridges([(0, 0), (0, 2), (2, 3)], TEST_DATA) == [
        [(0, 0), (0, 2), (2, 3), (3, 4)],
        [(0, 0), (0, 2), (2, 3), (3, 5)],
    ]
    assert get_next_bridges([(0, 0), (0, 2), (2, 2)], TEST_DATA) == [
        [(0, 0), (0, 2), (2, 2), (2, 3)]
    ]
    assert get_next_bridges([(0, 0), (0, 2), (2, 3), (3, 4)], TEST_DATA) == []
    assert get_next_bridges([(0, 0), (0, 2), (2, 3), (3, 5)], TEST_DATA) == []


def test_strength():
    assert (strength([(0, 0), (0, 1), (1, 10), (10, 9)])) == 31


def test_solution_1():
    assert solution_1(TEST_INPUT) == 31


def test_solution_2():
    assert solution_2(TEST_INPUT) == 19

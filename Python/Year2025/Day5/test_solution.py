from .solution import solution_1, solution_2, parse_input, is_fresh, join_range

TEST_INPUT = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

TEST_RANGES = [
    range(3, 6),
    range(10, 15),
    range(16, 21),
    range(12, 19),
]

TEST_IDS = [1, 5, 8, 11, 17, 32]


def test_parsing():
    ranges, ids = parse_input(TEST_INPUT)
    assert ranges == TEST_RANGES
    assert ids == TEST_IDS


def test_fresh():
    assert not is_fresh(1, TEST_RANGES)
    assert not is_fresh(8, TEST_RANGES)
    assert not is_fresh(32, TEST_RANGES)
    assert is_fresh(5, TEST_RANGES)
    assert is_fresh(11, TEST_RANGES)
    assert is_fresh(17, TEST_RANGES)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 3


def test_join_range():
    assert join_range(range(10, 15), range(14, 21)) == range(10, 21)
    assert join_range(range(14, 21), range(10, 15)) == range(10, 21)
    assert join_range(range(10, 21), range(14, 20)) == range(10, 21)
    assert join_range(range(14, 20), range(10, 21)) == range(10, 21)
    assert join_range(range(10, 15), range(15, 21)) is None


def test_solution_2():
    assert solution_2(TEST_INPUT) == 14

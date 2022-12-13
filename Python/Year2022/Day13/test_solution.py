from .solution import solution_1, solution_2, in_order

TEST_INPUT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


def test_list_smaller():
    # assert in_order([1, 1, 3, 1, 1], [1, 1, 5, 1, 1])
    # assert in_order([1, 1, 3, 2, 1], [1, 1, 5, 2, 1])
    # assert in_order([2, 3, 4], 4)
    # assert in_order([[1], [2, 3, 4]], [[1], 4])
    assert not in_order([9], [[8, 7, 6]])
    assert in_order([[4, 4], 4, 4], [[4, 4], 4, 4, 4])
    assert not in_order([7, 7, 7, 7], [7, 7, 7])
    assert in_order([], [3])
    assert not in_order([[[]]], [[]])
    assert not in_order(
        [1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]
    )

    assert not in_order(2, [[], 7, 8])
    assert in_order([[], 7, 8], 2)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 13


def test_solution_2():
    assert solution_2(TEST_INPUT) == 140

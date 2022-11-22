from .solution import knot_hash, knot_lst


def test_knot_lst_overflow():
    assert knot_lst([2, 1, 0, 3, 4], 3, 4) == [4, 3, 0, 1, 2]
    assert knot_lst([4, 3, 0, 1, 2], 1, 1) == [4, 3, 0, 1, 2]
    assert knot_lst([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]


def test_knot_lst():
    assert knot_lst([2, 1, 0, 3, 4], 0, 4) == [3, 0, 1, 2, 4]
    assert knot_lst([4, 3, 0, 1, 2], 3, 2) == [4, 3, 0, 2, 1]
    assert knot_lst([4, 3, 0, 1, 2], 0, 5) == [2, 1, 0, 3, 4]


def test_knot_hash():
    assert knot_hash(4, [3,4,1,5]) == [3,4,2,1,0]

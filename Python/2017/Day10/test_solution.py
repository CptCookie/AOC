from .solution import (
    knot_hash,
    knot_lst,
    parse_data_ascii,
    densening_hash,
    solution_2,
    convert_to_hex,
)


def test_knot_lst_overflow():
    assert knot_lst([2, 1, 0, 3, 4], 3, 4) == [4, 3, 0, 1, 2]
    assert knot_lst([4, 3, 0, 1, 2], 1, 1) == [4, 3, 0, 1, 2]
    assert knot_lst([4, 3, 0, 1, 2], 1, 5) == [3, 4, 2, 1, 0]


def test_knot_lst():
    assert knot_lst([2, 1, 0, 3, 4], 0, 4) == [3, 0, 1, 2, 4]
    assert knot_lst([4, 3, 0, 1, 2], 3, 2) == [4, 3, 0, 2, 1]
    assert knot_lst([4, 3, 0, 1, 2], 0, 5) == [2, 1, 0, 3, 4]


def test_knot_hash():
    assert knot_hash(4, [3, 4, 1, 5]) == [3, 4, 2, 1, 0]


def test_densening_hash():
    assert densening_hash([n for n in range(32)]) == [
        0 ^ 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 6 ^ 7 ^ 8 ^ 9 ^ 10 ^ 11 ^ 12 ^ 13 ^ 14 ^ 15,
        16 ^ 17 ^ 18 ^ 19 ^ 20 ^ 21 ^ 22 ^ 23 ^ 24 ^ 25 ^ 26 ^ 27 ^ 28 ^ 29 ^ 30 ^ 31,
    ]


def test_parse_data_bit():
    assert (parse_data_ascii("1,2,3")) == [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    assert parse_data_ascii("") == [17, 31, 73, 47, 23]


def test_convert_to_hex():
    assert convert_to_hex([255]) == "ff"
    assert convert_to_hex([64, 7, 255]) == "4007ff"


def test_knot_multi_empty():
    assert knot_hash(255, [], rounds=64) == list(n for n in range(256))


def test_knot_hash_multi():
    # ([0],1),2,3,4,5 pos 0, skip 0
    # 1,0,([2],3),4,5 pos 2, skipt 1
    # 1),0,3,2,4,([5] pos 5, skip 2
    # 5,0,3,([2],4),1 pos 4, skip 3
    # end round 1

    assert knot_hash(5, [2, 2, 2], rounds=1) == [5, 0, 3, 2, 4, 1]  # Round 1

    # 5,0,3,([2],4),1 pos 4, skip 3
    # 5,0,([3],4),2,1 pos 2, skip 4
    # 5,0,([4],3),2,1 pos 2, skip 5
    # 5,0,3,([4],2),1 pos 3, skip 6
    assert knot_hash(5, [2, 2, 2], rounds=2) == [5, 0, 3, 4, 2, 1]  # Round 2

    # 5,0,3,([4],2),1 pos 3, skip 6
    # 5),0,3,2,4,([1] pos 5, skip 7
    # 1,0,([3],2),4,5 pos 2, skip 8
    # 1,0,2,3,4,5
    assert knot_hash(5, [2, 2, 2], rounds=3) == [1, 0, 2, 3, 4, 5]  # Round 3


def test_solution_2():
    assert solution_2("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert solution_2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert solution_2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert solution_2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"

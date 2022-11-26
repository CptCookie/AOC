from .solution import get_differnces, number_valid_combinations


def test_differences_1():
    data = sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4, 0, 22])
    assert get_differnces(data) == [7, 0, 5]


def test_differences_2():
    data = sorted(
        [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3,
            0,
            52,
        ]
    )
    assert get_differnces(data) == [22, 0, 10]


def test_combinations():
    data = sorted([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])
    assert number_valid_combinations(data) == 8

from .solution import search_invalid, find_enryption_weakness


def test_search_invalid():
    puzzle = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert search_invalid(puzzle, 5) == 127


def test_search_weakness():
    puzzle = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert find_enryption_weakness(127, puzzle) == [15, 25, 47, 40]

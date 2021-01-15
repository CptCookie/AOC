from .solution import get_row, get_seat, get_ID


def test_row():
    assert get_row("FBFBBFF") == 44
    assert get_row("BFFFBBF") == 70
    assert get_row("FFFBBBF") == 14
    assert get_row("BBFFBBF") == 102


def test_seat():
    assert get_seat("RLR") == 5
    assert get_seat("RRR") == 7
    assert get_seat("RRR") == 7
    assert get_seat("RLL") == 4


def test_ID():
    assert get_ID("FBFBBFFRLR") == 357
    assert get_ID("BFFFBBFRRR") == 567
    assert get_ID("FFFBBBFRRR") == 119
    assert get_ID("BBFFBBFRLL") == 820

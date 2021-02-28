from .solution import Box


def test_wrapping_paper():
    assert Box(2, 3, 4).wrapping_needed() == 58
    assert Box(1, 1, 10).wrapping_needed() == 43


def test_ribbon():
    assert Box(2, 3, 4).ribbon_needed() == 34
    assert Box(1, 1, 10).ribbon_needed() == 14

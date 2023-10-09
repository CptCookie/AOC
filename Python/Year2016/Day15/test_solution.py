from .solution import lcm, time_alignment


def test_lcm():
    assert lcm(2, 3) == 6
    assert lcm(2, 6) == 6
    assert lcm(3, 6) == 6
    assert lcm(4, 6) == 12


def test_allignment():
    assert time_alignment([(5, 4), (2, 1), (3, 0)]) == 15
    assert time_alignment([(5, 4), (2, 1)]) == 5

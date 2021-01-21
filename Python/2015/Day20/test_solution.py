from .solution import get_lowest_house


def test_lowest_house():
    assert get_lowest_house(10) == 1
    assert get_lowest_house(30) == 2
    assert get_lowest_house(40) == 3
    assert get_lowest_house(70) == 4
    assert get_lowest_house(60) == 4
    assert get_lowest_house(120) == 6
    assert get_lowest_house(80) == 6
    assert get_lowest_house(150) == 8
    assert get_lowest_house(130) == 8
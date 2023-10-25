from .solution import is_alternating


def test_alternating():
    assert is_alternating([0, 1, 0, 1, 1]) == False
    assert is_alternating([0, 1, 0, 1, 0]) == True
    assert is_alternating([1, 0, 1, 0, 1]) == False
    assert is_alternating([0, 1, 0, 2, 0]) == False

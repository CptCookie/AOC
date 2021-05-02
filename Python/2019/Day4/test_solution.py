from .solution import solution_2, contains_double, is_not_descending, contains_multiple


def test_ascending():
    assert is_not_descending(12)
    assert is_not_descending(123456)
    assert is_not_descending(111111)
    assert is_not_descending(123789)
    assert not is_not_descending(123780)
    assert not is_not_descending(987654)


def test_double():
    assert contains_double(11)
    assert not contains_double(111111)
    assert contains_double(122345)
    assert not contains_double(123789)
    assert not contains_double(135679)


def test_multiple():
    assert contains_multiple(11)
    assert contains_multiple(111111)
    assert contains_multiple(122345)
    assert not contains_multiple(123789)
    assert not contains_multiple(135679)
from .solution import find_hash


def test_hash():
    assert find_hash("abcdef", 5) == 609043
    assert find_hash("pqrstuv", 5) == 1048970

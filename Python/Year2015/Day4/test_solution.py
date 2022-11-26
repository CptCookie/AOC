from .solution import find_hash_with_leeding_zeros


def test_hash():
    assert find_hash_with_leeding_zeros("abcdef", leeding_zeros=5) == 609043
    assert find_hash_with_leeding_zeros("pqrstuv", leeding_zeros=5) == 1048970

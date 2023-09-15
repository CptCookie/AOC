from .solution import get_combo_char, hash_valid, get_hashes, get_stretched_hash


def test_combo():
    assert get_combo_char("123456", 3) is None
    assert get_combo_char("12333456", 3) == "3"
    assert get_combo_char("33435", 3) is None
    assert get_combo_char("3333456", 4) == "3"
    assert get_combo_char("133333456", 5) == "3"


def test_hash_validation():
    assert hash_valid("abc", 18) is False
    assert hash_valid("abc", 39) is True
    assert hash_valid("abc", 92) is True


def test_hash_validation_stretch():
    assert hash_valid("abc", 5, stretched=True) is False
    assert hash_valid("abc", 10, stretched=True) is True
    assert hash_valid("abc", 22551, stretched=True) is True


def test_streched_hash():
    assert get_stretched_hash("abc", 0) == "a107ff634856bb300138cac6568c0f24"
    assert "eee" in get_stretched_hash("abc", 10)
    assert "eeeee" in get_stretched_hash("abc", 89)
    assert "fff" in get_stretched_hash("abc", 22551)
    assert "fffff" in get_stretched_hash("abc", 22859)


def test_get_hashes():
    assert get_hashes("abc")[-1] == 22728

from .solution import get_pw, get_pw_v2, get_md5_hash


def test_get_hash():
    assert get_md5_hash("abc3231929")[:5] == "00000"


def test_get_pw():
    assert get_pw("abc") == "18f47a30"


def test_get_pw_2():
    assert get_pw_v2("abc") == "05ace8e3"

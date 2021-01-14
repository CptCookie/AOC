from solution import count_code, count_char, count_reencode


def test_count_code():
    assert count_code(r'""') == 2
    assert count_code(r'"abc"') == 5
    assert count_code(r'"aaa\"aaa"') == 10
    assert count_code(r'"\x27"') == 6


def test_count_char():
    assert count_char(r'""') == 0
    assert count_char(r'"abc"') == 3
    assert count_char(r'"aaa\"aaa"') == 7
    assert count_char(r'"\x27"') == 1


def test_count_reencode():
    assert count_reencode(r'""') == 6
    assert count_reencode(r'"abc"') == 9
    assert count_reencode(r'"aaa\"aaa"') == 16
    assert count_reencode(r'"\x27"') == 11
    assert count_reencode(r'"\\"') == 10

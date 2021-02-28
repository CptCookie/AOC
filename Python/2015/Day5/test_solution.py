from .solution import has_two_apart, has_double, is_valid_string_v1, is_valid_string_v2


def test_has_double():
    assert has_double("xxyxx") == True
    assert has_double("abxxxjf") == False
    assert has_double("xx") == False


def test_two_apart():
    assert has_two_apart("xyx") == True
    assert has_two_apart("qjhvhtzxzqqjkmpb") == True
    assert has_two_apart("uurcxstgmygtbstg") == False


def test_is_valid_string_v1():
    assert is_valid_string_v1("ugknbfddgicrmopn") == True
    assert is_valid_string_v1("jchzalrnumimnmhp") == False
    assert is_valid_string_v1("haegwjzuvuyypxyu") == False
    assert is_valid_string_v1("dvszwmarrgswjxmb") == False


def test_is_valid_string_v2():
    assert is_valid_string_v2("qjhvhtzxzqqjkmpb") == True
    assert is_valid_string_v2("xxyxx") == True
    assert is_valid_string_v2("uurcxstgmygtbstg") == False
    assert is_valid_string_v2("ieodomkazucvgmuy") == False

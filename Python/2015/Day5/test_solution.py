from solution import has_two_apart, has_double, is_naughty_new, is_naughty_old


def test_has_double():
    assert has_double("xxyxx") == True
    assert has_double("abxxxjf") == False
    assert has_double("xx") == False


def test_two_apart():
    assert has_two_apart("xyx") == True
    assert has_two_apart("qjhvhtzxzqqjkmpb") == True
    assert has_two_apart("uurcxstgmygtbstg") == False


def test_naughty_old():
    assert is_naughty_old("ugknbfddgicrmopn") == False
    assert is_naughty_old("jchzalrnumimnmhp") == True
    assert is_naughty_old("haegwjzuvuyypxyu") == True
    assert is_naughty_old("dvszwmarrgswjxmb") == True


def test_naughty_new():
    assert is_naughty_new("qjhvhtzxzqqjkmpb") == False
    assert is_naughty_new("xxyxx") == False
    assert is_naughty_new("uurcxstgmygtbstg") == True
    assert is_naughty_new("ieodomkazucvgmuy") == True

from .solution import contains_abba, supports_abba, supports_ssl, get_babs


def test_abba():
    assert contains_abba("abba") == True
    assert contains_abba("xsabbaxyz") == True
    assert contains_abba("abcd") == False
    assert contains_abba("aaaa") == False
    assert contains_abba("abaa") == False
    assert contains_abba("aaba") == False
    assert contains_abba("aabb") == False
    assert contains_abba("abbc") == False
    assert contains_abba("abca") == False
    assert contains_abba("abab") == False


def test_support_abba():
    assert supports_abba(["abba", "mnop", "qrst"]) == True
    assert supports_abba(["ioxxoj", "asdfgh", "zxcvbn"]) == True
    assert supports_abba(["abcd", "bddb', 'xyyx"]) == False
    assert supports_abba(["aaaa", "qwer", "tyui"]) == False
    assert supports_abba(["abba", "xyz", "abba", "xyz", "abba"]) == True


def test_contains_bab():
    assert get_babs(["aba"]) == ["aba"]
    assert get_babs(["bab"]) == ["bab"]
    assert get_babs(["xyx"]) == ["xyx"]
    assert get_babs(["zazbz"]) == ["zaz", "zbz"]
    assert get_babs(["zaz", "zbz"]) == ["zaz", "zbz"]
    assert get_babs(["xxx"]) == []
    assert get_babs(["yyx"]) == []


def test_support_ssl():
    assert supports_ssl(["aba", "bab", "xyz"]) == True
    assert supports_ssl(["xyx", "xyx", "xyx"]) == False
    assert supports_ssl(["aaa", "kek", "eke"]) == True
    assert supports_ssl(["zazbz", "bzb", "cdb"]) == True

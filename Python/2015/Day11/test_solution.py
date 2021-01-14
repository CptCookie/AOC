from solution import is_valid, increment


def test_is_valid():
    assert is_valid("aabcc") == True
    assert is_valid("aabc") == False
    assert is_valid("aaabc") == False
    assert is_valid("aabbc") == False
    assert is_valid("hijklmmn") == False
    assert is_valid("abbceffg") == False
    assert is_valid("abbcegjk") == False
    assert is_valid("abcdffaa") == True
    assert is_valid("ghjaabcc") == True


def test_increment():
    assert increment("z").__next__() == "aa"
    assert increment("aaaz").__next__() == "aaba"
    assert increment("abc").__next__() == "abd"

from .solution import solution_1, solution_2, no_duplication, no_anagrams


def test_no_duplication():
    assert no_duplication("aa bb cc dd ee")
    assert not no_duplication("aa bb cc dd ee aa")
    assert no_duplication("aa bb cc dd ee aaa")


def test_no_anagram():
    assert no_anagrams("abcde fghij")
    assert no_anagrams("a ab abc abd abf abj")
    assert no_anagrams("iiii oiii ooii oooi oooo")
    assert not no_anagrams("abcde xyz ecdab")
    assert not no_anagrams("oiii ioii iioi iiio")


def test_solution_1():
    assert solution_1("aa bb cc\naa bb aa\naa bb aaa") == 2


def test_solution_2():
    assert solution_2("ab bb cc\nab bb aa\nab bb ba") == 2

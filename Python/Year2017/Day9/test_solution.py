from .solution import solution_1, solution_2, remove_invert, remove_garbage, count_value


def test_remove_invert():
    assert remove_invert('<{o"i!a,<{i<a>') == '<{o"i,<{i<a>'
    assert remove_invert("!!") == ""
    assert remove_invert("<!!!>>") == "<>"


def test_remove_garbage():
    assert remove_garbage("!!") == ("", 0)
    assert remove_garbage("<!!!>>") == ("", 0)
    assert remove_garbage("<>") == ("", 0)
    assert remove_garbage("<random characters>") == ("", 17)
    assert remove_garbage("<<<<>") == ("", 3)
    assert remove_garbage("<{!>}>") == ("", 2)
    assert remove_garbage("<!!>") == ("", 0)
    assert remove_garbage("<!!!>>") == ("", 0)
    assert remove_garbage("<{o'i!a,<{i<a>") == ("", 10)
    assert remove_garbage("{{<{o'i!a,<{i<a>},{<{o'i!a,<{i<a>}}") == ("{{},{}}", 20)


def test_value():
    assert count_value('<{o"i!a,<{i<a>abc') == 0
    assert count_value("!!") == 0
    assert count_value("<!!!>>") == 0

    assert count_value("{}") == 1
    assert count_value("{{{}}}") == 6
    assert count_value("{{},{}}") == 5
    assert count_value("{{{},{},{{}}}}") == 16
    assert count_value("{<{},{},{{}}>}") == 1
    assert count_value("{<a>,<a>,<a>,<a>}") == 1
    assert count_value("{{<a>},{<a>},{<a>},{<a>}}") == 9
    assert count_value("{{<!>},{<!>},{<!>},{<a>}}") == 3

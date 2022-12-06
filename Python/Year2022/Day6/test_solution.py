from .solution import find_destinct_chars


def test_find_destinct_char_4():
    assert find_destinct_chars("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert find_destinct_chars("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert find_destinct_chars("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert find_destinct_chars("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11


def test_find_destinct_char_14():
    assert find_destinct_chars("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19
    assert find_destinct_chars("bvwbjplbgvbhsrlpgdmjqwftvncz", 14) == 23
    assert find_destinct_chars("nppdvjthqldpwncqszvftbrmjlhg", 14) == 23
    assert find_destinct_chars("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14) == 29
    assert find_destinct_chars("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14) == 26

from .solution import solution_1, solution_2, find_start


def test_find_start():
    assert find_start("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_start("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_start("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_start("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_solution_1():
    test_input = ""
    assert solution_1(test_input)


def test_solution_2():
    test_input = ""
    assert solution_2(test_input)

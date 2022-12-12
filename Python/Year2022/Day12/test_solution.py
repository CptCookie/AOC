from .solution import solution_1, solution_2, parse_data

TEST_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


def test_parse():
    map, start, end = parse_data(TEST_INPUT)
    string_map = "\n".join("".join(line) for line in map)
    expected_map = TEST_INPUT.replace("S", "a").replace("E", "z")
    assert string_map == expected_map
    assert start == (0, 0)
    assert end == (5, 2)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 31


def test_solution_2():
    test_input = ""
    assert solution_2(test_input)

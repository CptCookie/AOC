from .solution import solution_1, solution_2, get_antinodes, parse_input

TEST_INPUT = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

TEST_DATA = {"0": [(8, 1), (5, 2), (7, 3), (4, 4)], "A": [(6, 5), (8, 8), (9, 9)]}


def test_anitnodes():
    assert get_antinodes([(1, 1), (2, 2)], (5, 5)) == [(0, 0), (3, 3)]
    assert get_antinodes([(1, 1), (3, 3)], (6, 6)) == [(5, 5)]
    assert get_antinodes([(2, 2), (2, 3), (3, 2)], (6, 6)) == [
        (2, 1),
        (2, 4),
        (1, 2),
        (4, 2),
        (1, 4),
        (4, 1),
    ]


def test_parsing():
    antennas, dimensions = parse_input(TEST_INPUT)
    assert antennas == TEST_DATA
    assert dimensions == (12, 12)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 14


def test_solution_2():
    assert solution_2(TEST_INPUT) == 34

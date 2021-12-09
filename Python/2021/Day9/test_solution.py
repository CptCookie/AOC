from .solution import HeightMap, parse_input, solution_1, solution_2

test_input = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"


def test_parse():
    expected = [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]
    assert parse_input(test_input) == expected


def test_get_adj():
    h_map = HeightMap(parse_input(test_input))
    assert h_map.get_adj(1, 0) == [2, 9, 9]


def test_get_adj():
    h_map = HeightMap(parse_input(test_input))
    assert h_map.get_lowst_points() == [(1, 0), (2, 2), (6, 4), (9, 0)]


def test_pool_1():
    h_map = HeightMap(parse_input(test_input))
    assert h_map.get_pool_points(1, 0, []) == [(0, 0), (1, 0), (0, 1)]


def test_solution_1():
    assert solution_1(test_input) == 15


def test_solution_2():
    assert solution_2(test_input) == 1134

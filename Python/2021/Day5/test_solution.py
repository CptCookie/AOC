from .solution import solution_1, solution_2, HydroMap, parse_data

test_data = """0,9 -> 5,9\n8,0 -> 0,8\n9,4 -> 3,4\n2,2 -> 2,1\n7,0 -> 7,4\n6,4 -> 2,0\n0,9 -> 2,9\n3,4 -> 1,4\n0,0 -> 8,8\n5,5 -> 8,2\n"""


def test_draw_map():
    hydro_map = HydroMap(4)
    hydro_map.draw_line((1, 1), (1, 3))

    assert hydro_map.map == [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]


def test_draw_map():
    hydro_map = HydroMap(4)
    hydro_map.draw_line((1, 1), (3, 3), diagonal=True)

    assert hydro_map.map == [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]


def test_parse_data():
    expected = [
        ((0, 9), (5, 9)),
        ((8, 0), (0, 8)),
        ((9, 4), (3, 4)),
        ((2, 2), (2, 1)),
        ((7, 0), (7, 4)),
        ((6, 4), (2, 0)),
        ((0, 9), (2, 9)),
        ((3, 4), (1, 4)),
        ((0, 0), (8, 8)),
        ((5, 5), (8, 2)),
    ]
    assert parse_data(test_data) == expected


def test_solution_1():
    assert solution_1(test_data) == 5


def test_solution_2():
    assert solution_2(test_data) == 12

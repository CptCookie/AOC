from .solution import solution_1, solution_2, parse_map, find_nodes, get_route

TEST_INPUT = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########
"""

TEST_DATA = [
    "###########",
    "#0.1.....2#",
    "#.#######.#",
    "#4.......3#",
    "###########",
]


def test_parsing():
    assert parse_map(TEST_INPUT) == TEST_DATA


def test_find_node():
    assert find_nodes(TEST_DATA) == {
        "0": (1, 1),
        "1": (3, 1),
        "2": (9, 1),
        "4": (1, 3),
        "3": (9, 3),
    }


def test_route():
    assert get_route(
        TEST_DATA,
        (1, 1),
        (9, 2),
    ) == [(2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (9, 2)]


def test_route_corner():
    assert get_route(
        [
            "#####",
            "#0..#",
            "#.#.#",
            "#...#",
            "#.1##",
            "#####",
        ],
        (1, 1),
        (2, 4),
    ) == [(1, 2), (1, 3), (1, 4), (2, 4)]


def test_route_corner():
    assert get_route(
        [
            "#####",
            "#0..#",
            "#..1#",
            "#...#",
            "#.1##",
            "#####",
        ],
        (1, 1),
        (2, 4),
    ) == [(1, 2), (1, 3), (1, 4), (2, 4)]


def test_route_TEST_DATA():
    nodes = find_nodes(TEST_DATA)

    assert len(get_route(TEST_DATA, nodes["0"], nodes["4"])) == 2
    assert len(get_route(TEST_DATA, nodes["4"], nodes["1"])) == 4
    assert len(get_route(TEST_DATA, nodes["1"], nodes["2"])) == 6
    assert len(get_route(TEST_DATA, nodes["2"], nodes["3"])) == 2


def test_solution_1():
    assert solution_1(TEST_INPUT) == 14


def test_solution_2():
    assert solution_2(TEST_INPUT)

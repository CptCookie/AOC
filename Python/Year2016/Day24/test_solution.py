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
    assert get_route(TEST_DATA, (1, 1), (9, 2)) == 9


def test_route_corner():
    test_map = ["#####", "#0..#", "#.#.#", "#...#", "#.1##", "#####"]
    assert get_route(test_map, (1, 1), (2, 4)) == 4


def test_route_open():
    test_map = ["#####", "#0..#", "#..1#", "#####"]
    assert get_route(test_map, (1, 1), (3, 2)) == 3


def test_solution_1():
    assert solution_1(TEST_INPUT) == 14

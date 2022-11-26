from .solution import (
    get_path,
    get_closest_intersection_distance,
    get_shortest_intersection_steps_comb,
)

TEST_CABLES_1 = [
    ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"],
    ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"],
]

TEST_CABLES_2 = [
    ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"],
    ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"],
]


def test_get_path():
    assert get_path(["R1"]) == [(1, 0)]
    assert get_path(["L1"]) == [(-1, 0)]
    assert get_path(["U1"]) == [(0, 1)]
    assert get_path(["D1"]) == [(0, -1)]
    assert get_path(["R2", "L2"]) == [(1, 0), (2, 0), (1, 0), (0, 0)]
    assert get_path(["U2", "D2"]) == [(0, 1), (0, 2), (0, 1), (0, 0)]


def test_instersection_distance_example():
    cable_1 = get_path(["R8", "U5", "L5", "D3"])
    cable_2 = get_path(["U7", "R6", "D4", "L4"])

    assert get_closest_intersection_distance(cable_1, cable_2) == 6


def test_instersection_distance_cable_1():
    cable_1 = get_path(TEST_CABLES_1[0])
    cable_2 = get_path(TEST_CABLES_1[1])

    assert get_closest_intersection_distance(cable_1, cable_2) == 159


def test_instersection_distance_cable_2():
    cable_1 = get_path(TEST_CABLES_2[0])
    cable_2 = get_path(TEST_CABLES_2[1])

    assert get_closest_intersection_distance(cable_1, cable_2) == 135


def test_shortest_instersection_example():
    cable_1 = get_path(["R8", "U5", "L5", "D3"])
    cable_2 = get_path(["U7", "R6", "D4", "L4"])

    assert get_shortest_intersection_steps_comb(cable_1, cable_2) == 30


def test_shortest_instersection_cable_1():
    cable_1 = get_path(TEST_CABLES_1[0])
    cable_2 = get_path(TEST_CABLES_1[1])

    assert get_shortest_intersection_steps_comb(cable_1, cable_2) == 610


def test_shortest_instersection_cable_2():
    cable_1 = get_path(TEST_CABLES_2[0])
    cable_2 = get_path(TEST_CABLES_2[1])

    assert get_shortest_intersection_steps_comb(cable_1, cable_2) == 410

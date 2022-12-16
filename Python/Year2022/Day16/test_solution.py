from .solution import solution_1, solution_2, parse_input, transform_net

TEST_INPUT = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""

TEST_DATA = {
    "AA": (0, ["DD", "II", "BB"]),
    "BB": (13, ["CC", "AA"]),
    "CC": (2, ["DD", "BB"]),
    "DD": (20, ["CC", "AA", "EE"]),
    "EE": (3, ["FF", "DD"]),
    "FF": (0, ["EE", "GG"]),
    "GG": (0, ["FF", "HH"]),
    "HH": (22, ["GG"]),
    "II": (0, ["AA", "JJ"]),
    "JJ": (21, ["II"]),
    }

TEST_TRANSFORMED_DATA = {
    "BB": {
        "CC": 1,
        "DD": 2,
        "EE": 3,
        "HH": 6,
        "JJ": 3,
        },
    "CC": {
        "BB": 1,
        "DD": 1,
        "EE": 2,
        "HH": 5,
        "JJ": 4,
        },
    "DD": {
        "BB": 2,
        "CC": 1,
        "EE": 1,
        "HH": 4,
        "JJ": 3,
        },
    "EE": {
        "BB": 3,
        "CC": 2,
        "DD": 1,
        "HH": 3,
        "JJ": 4,
        },
    "HH": {
        "BB": 6,
        "CC": 5,
        "DD": 4,
        "EE": 3,
        "JJ": 7,
        },
    "JJ": {
        "BB": 3,
        "CC": 4,
        "DD": 3,
        "EE": 4,
        "HH": 7,
        },

    }


#
# def test_parsing():
#     assert parse_input(TEST_INPUT) == TEST_DATA

def test_transform_network():
    assert transform_net(TEST_DATA) == TEST_TRANSFORMED_DATA

#
# def test_solution_1():
#     assert solution_1(TEST_INPUT)
#
#
# def test_solution_2():
#     assert solution_2(TEST_INPUT)

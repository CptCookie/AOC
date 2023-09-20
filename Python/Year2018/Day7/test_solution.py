from copy import deepcopy

from .solution import solution_1, solution_2, parse_input, get_route_parallel

TEST_INPUT = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
"""

TEST_DATA = [
    ("C", "A"),
    ("C", "F"),
    ("A", "B"),
    ("A", "D"),
    ("B", "E"),
    ("D", "E"),
    ("F", "E"),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == "CABDFE"


def test_solution_2():
    assert get_route_parallel(deepcopy(TEST_DATA), 2, 0) == 15
    assert get_route_parallel(deepcopy(TEST_DATA), 3, 0) == 14
    assert get_route_parallel(deepcopy(TEST_DATA), 5, 60) == 253

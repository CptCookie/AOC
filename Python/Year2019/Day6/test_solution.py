from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

TEST_DATA = [
    ("COM", "B"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("E", "F"),
    ("B", "G"),
    ("G", "H"),
    ("D", "I"),
    ("E", "J"),
    ("J", "K"),
    ("K", "L"),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 42


def test_solution_2():
    assert solution_2(TEST_INPUT)

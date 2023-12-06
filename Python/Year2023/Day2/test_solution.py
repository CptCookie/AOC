from .solution import solution_1, solution_2, parse_input, pow_min_cubes

TEST_INPUT = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

TEST_DATA = [
    [
        [(3, "blue"), (4, "red")],
        [(1, "red"), (2, "green"), (6, "blue")],
        [(2, "green")],
    ],
    [
        [(1, "blue"), (2, "green")],
        [(3, "green"), (4, "blue"), (1, "red")],
        [(1, "green"), (1, "blue")],
    ],
    [
        [(8, "green"), (6, "blue"), (20, "red")],
        [(5, "blue"), (4, "red"), (13, "green")],
        [(5, "green"), (1, "red")],
    ],
    [
        [(1, "green"), (3, "red"), (6, "blue")],
        [(3, "green"), (6, "red")],
        [(3, "green"), (15, "blue"), (14, "red")],
    ],
    [[(6, "red"), (1, "blue"), (3, "green")], [(2, "blue"), (1, "red"), (2, "green")]],
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 8


def test_pow_game():
    assert pow_min_cubes(TEST_DATA[0]) == 48
    assert pow_min_cubes(TEST_DATA[1]) == 12
    assert pow_min_cubes(TEST_DATA[2]) == 1560
    assert pow_min_cubes(TEST_DATA[3]) == 630
    assert pow_min_cubes(TEST_DATA[4]) == 36


def test_solution_2():
    assert solution_2(TEST_INPUT) == 2286

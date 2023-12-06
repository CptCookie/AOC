from .solution import (
    solution_1,
    solution_2,
    parse_individual,
    get_num_win_moves,
    parse_total,
)

TEST_INPUT = """Time:      7  15   30
Distance:  9  40  200
"""

TEST_DATA = [(7, 9), (15, 40), (30, 200)]


def test_parsing_individual():
    assert parse_individual(TEST_INPUT) == TEST_DATA


def test_parsing_total():
    assert parse_total(TEST_INPUT) == (71530, 940200)


def test_winning_move():
    assert get_num_win_moves((7, 9)) == 4
    assert get_num_win_moves((15, 40)) == 8
    assert get_num_win_moves((30, 200)) == 9
    assert get_num_win_moves((71530, 940200)) == 71503


def test_solution_1():
    assert solution_1(TEST_INPUT) == 288


def test_solution_2():
    assert solution_2(TEST_INPUT) == 71503

from .solution import (
    solution_1,
    get_position,
    get_start_number_of_layer,
    get_adjacent_positions,
)


def test_get_adjacent_positions():
    adjacent = get_adjacent_positions(0, 0)
    expected = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1)]

    for ex in expected:
        print(ex)
        assert ex in adjacent
    assert len(adjacent) == len(expected)


def test_start_number():
    assert get_start_number_of_layer(2) == 2
    assert get_start_number_of_layer(3) == 10


def test_iterative_position():
    """
    5   4   3
    6   1   2
    7   8   9
    """
    assert get_position(1) == (0, 0)
    assert get_position(2) == (1, 0)
    assert get_position(3) == (1, 1)
    assert get_position(4) == (0, 1)
    assert get_position(5) == (-1, 1)
    assert get_position(6) == (-1, 0)
    assert get_position(7) == (-1, -1)
    assert get_position(8) == (0, -1)
    assert get_position(9) == (1, -1)


def test_solution_1():
    assert solution_1("1") == 0
    assert solution_1("12") == 3
    assert solution_1("23") == 2
    assert solution_1("1024") == 31

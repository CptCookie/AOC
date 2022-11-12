from .solution import Routing, solution_1, solution_2
from .solution import NORTH, EAST, SOUTH, WEST


def test_solution_1():
    assert solution_1("R2, L3") == 5
    assert solution_1("R2, R2, R2") == 2
    assert solution_1("R5, L5, R5, R3") == 12


def test_solution_2():
    assert solution_2("R8, R4, R4, R8") == 4


def test_log_1():
    route = Routing()
    route.direction = EAST
    route.move(4)

    assert route.visited == [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]


def test_log_2():
    route = Routing()
    route.direction = NORTH
    route.move(4)

    assert route.visited == [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]


def test_log_3():
    route = Routing()
    route.direction = WEST
    route.move(4)

    assert route.visited == [(0, 0), (-1, 0), (-2, 0), (-3, 0), (-4, 0)]


def test_log_4():
    route = Routing()
    route.direction = SOUTH
    route.move(4)

    assert route.visited == [(0, 0), (0, -1), (0, -2), (0, -3), (0, -4)]


def test_move_with_log():
    puzzle_input = ["R8", "R4", "R4", "R8"]
    route = Routing()

    for p in puzzle_input:
        if p[0] == "R":
            route.turn_right()
        if p[0] == "L":
            route.turn_left()
        route.move(int(p[1:]))

    assert route.visited == [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (6, 0),
        (7, 0),
        (8, 0),
        (8, -1),
        (8, -2),
        (8, -3),
        (8, -4),
        (7, -4),
        (6, -4),
        (5, -4),
        (4, -4),
        (4, -3),
        (4, -2),
        (4, -1),
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
    ]


if __name__ == "__main__":
    test_solution_2()

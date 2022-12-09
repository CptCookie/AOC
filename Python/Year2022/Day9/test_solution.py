from .solution import solution_1, Rope

TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

TEST_DATA = [
    ["R", "4"],
    ["U", "4"],
    ["L", "3"],
    ["D", "1"],
    ["R", "4"],
    ["D", "1"],
    ["L", "5"],
    ["R", "2"],
]


def test_move_tail_touching():
    r = Rope()
    r.knots = [(2, 1), (1, 1)]

    r._move_tail()
    assert r.knots[-1] == (1, 1)


def test_move_tail_horizontal_neg():
    r = Rope()
    r.knots = [(1, 1), (3, 1)]
    r._move_tail()
    assert r.knots[-1] == (2, 1)


def test_move_tail_vertical():
    r = Rope()
    r.knots = [(1, 3), (1, 1)]

    r._move_tail()
    assert r.knots[-1] == (1, 2)


def test_move_tail_vertical_neg():
    r = Rope()
    r.knots = [(1, 1), (1, 3)]
    r._move_tail()
    assert r.knots[-1] == (1, 2)


def test_move_tail_diag_45_deg():
    r = Rope()
    r.knots = [(3, 3), (1, 1)]
    r._move_tail()
    assert r.knots[-1] == (2, 2)


def test_move_tail_diag_ver():
    r = Rope()
    r.knots = [(2, 3), (1, 1)]
    r._move_tail()
    assert r.knots[-1] == (2, 2)


def test_move_tail_diag_hor():
    r = Rope()
    r.knots = [(3, 2), (1, 1)]
    r._move_tail()
    assert r.knots[-1] == (2, 2)


def test_move_same():
    r = Rope()
    r.knots = [(1, 1), (1, 1)]
    r._move_tail()
    assert r.knots[-1] == (1, 1)


def test_move_combo():
    r = Rope()
    r.knots = [(3, 3), (1, 1), (0, 0)]
    r._move_tail()
    assert r.knots == [(3, 3), (2, 2), (1, 1)]


def test_move_short():
    r = Rope()
    r.move(TEST_DATA[0])

    assert r.knots[0] == (4, 0)
    assert r.knots[1] == (3, 0)


def test_move():
    r = Rope()
    r.move_all(TEST_DATA)

    assert r.knots[0] == (2, 2)
    assert r.knots[1] == (1, 2)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 13

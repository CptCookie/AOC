from .solution import solution_1, solution_2, Map


def test_built_walls():
    m = Map([[(498, 4), (498, 6), (496, 6)]])
    assert m.map == [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "#"],
        [".", ".", "#"],
        ["#", "#", "#"],
    ]


def test_built_walls_2():
    m = Map([[(498, 4), (498, 6), (496, 6)], [(503, 4), (502, 4), (502, 9), (494, 9)]])
    assert m.map == [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "#", ".", ".", ".", "#", "#"],
        [".", ".", ".", ".", "#", ".", ".", ".", "#", "."],
        [".", ".", "#", "#", "#", ".", ".", ".", "#", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "."],
    ]


def test_pour_in_sand():
    m = Map([[(498, 4), (498, 6), (496, 6)], [(503, 4), (502, 4), (502, 9), (494, 9)]])
    assert m.pour_in_sand((500, 0)) == 24
    assert m.map == [
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", "o", ".", ".", "."],
        [".", ".", ".", ".", ".", "o", "o", "o", ".", "."],
        [".", ".", ".", ".", "#", "o", "o", "o", "#", "#"],
        [".", ".", ".", "o", "#", "o", "o", "o", "#", "."],
        [".", ".", "#", "#", "#", "o", "o", "o", "#", "."],
        [".", ".", ".", ".", "o", "o", "o", "o", "#", "."],
        [".", "o", ".", "o", "o", "o", "o", "o", "#", "."],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "."],
    ]


def test_pour_in_sand_limit():
    m = Map(
        [[(498, 4), (498, 6), (496, 6)], [(503, 4), (502, 4), (502, 9), (494, 9)]],
        endless=False,
    )
    assert m.pour_in_sand((500, 0)) == 92

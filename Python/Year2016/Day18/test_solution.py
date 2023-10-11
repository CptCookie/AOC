from .solution import solution_1, solution_2, build_map


def test_map():
    assert build_map("..^^.", 3) == ["..^^.", ".^^^^", "^^..^"]
    assert build_map(".^^.^.^^^^", 10) == [
        ".^^.^.^^^^",
        "^^^...^..^",
        "^.^^.^.^^.",
        "..^^...^^^",
        ".^^^^.^^.^",
        "^^..^.^^..",
        "^^^^..^^^.",
        "^..^^^^.^^",
        ".^^^..^.^^",
        "^^.^^^..^^",
    ]


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT)

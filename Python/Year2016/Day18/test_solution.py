from .solution import build_map


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

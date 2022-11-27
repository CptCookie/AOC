from .solution import solution_1, solution_2, DanceGroup


def test_spin():
    d = DanceGroup()
    d.spin(5)
    assert "".join(d.dancers) == "lmnopabcdefghijk"


def test_excange():
    d = DanceGroup()
    d.excange(13, 2)
    assert "".join(d.dancers) == "abndefghijklmcop"


def test_partner():
    d = DanceGroup()
    d.partner("e", "i")
    assert "".join(d.dancers) == "abcdifghejklmnop"


def test_dance():
    d = DanceGroup()
    d.dancers = ["a", "b", "c", "d", "e"]
    d.dance(["s1", "x3/4", "pe/b"])

    assert "".join(d.dancers) == "baedc"

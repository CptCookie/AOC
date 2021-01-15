from .solution import match, parse_aunts, FEWER, EXACT, GREATER


def test_parse():
    s = "Sue 1: goldfish: 6, trees: 9, akitas: 0\nSue 2: goldfish: 7, trees: 1, akitas: 0"
    assert parse_aunts(s) == [
        {"goldfish": 6, "trees": 9, "akitas": 0},
        {"goldfish": 7, "trees": 1, "akitas": 0},
    ]


def test_match():
    remember = {"a": 1, "b": 0}
    aunts = [{"a": 2}, {"b": 0}]
    assert match(aunts, remember) == 2


def test_retro():
    remember = {"a": 1, "b": 0}
    retro = {"a": GREATER, "b": FEWER}
    aunts = [{"a": 2}, {"b": 0}]
    assert match(aunts, remember, retro) == 1

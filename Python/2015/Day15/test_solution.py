from .solution import get_cookie_score, max_score_cookie
from pytest import skip


def test_cookie_score():
    ingr = {
        "B": {"c": -1, "d": -2, "f": 6, "t": 3, "calories": 8},
        "C": {"c": 2, "d": 3, "f": -2, "t": -1, "calories": 3},
    }
    cookie = {"B": 44, "C": 56}
    assert get_cookie_score(cookie, ingr) == 62842880


def test_max_score():
    ingr = {
        "B": {"c": -1, "d": -2, "f": 6, "t": 3, "calories": 8},
        "C": {"c": 2, "d": 3, "f": -2, "t": -1, "calories": 3},
    }
    assert max_score_cookie(ingr) == 62842880


def test_max_score_weight_watch():
    ingr = {
        "B": {"c": -1, "d": -2, "f": 6, "t": 3, "calories": 8},
        "C": {"c": 2, "d": 3, "f": -2, "t": -1, "calories": 3},
    }
    assert max_score_cookie(ingr, True) == 57600000
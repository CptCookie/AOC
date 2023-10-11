from .solution import (
    play_white_elephant_easy,
    play_white_elephant_complex,
)


def test_solution_1():
    assert play_white_elephant_easy(5) == 3


def test_solution_2():
    assert play_white_elephant_complex(5) == 2
    assert play_white_elephant_complex(16) == 7
    assert play_white_elephant_complex(27) == 27

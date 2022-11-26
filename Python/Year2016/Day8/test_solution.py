from .solution import Display


def test_rect_1():
    display = Display(3, 2)
    display.rect(2, 1)

    assert display.pixels == [[True, True, False], [False, False, False]]


def test_rect_2():
    display = Display(4, 3)
    display.rect(3, 2)

    assert display.pixels == [
        [True, True, True, False],
        [True, True, True, False],
        [False, False, False, False],
    ]


def test_shift_row_1():
    display = Display(4, 3)
    display.rect(3, 2)
    display.shift_row(0, 2)

    assert display.pixels == [
        [True, False, True, True],
        [True, True, True, False],
        [False, False, False, False],
    ]


def test_shift_col_1():
    display = Display(4, 3)
    display.rect(3, 2)
    display.shift_column(1, 2)

    assert display.pixels == [
        [True, True, True, False],
        [True, False, True, False],
        [False, True, False, False],
    ]


def test_parse_rect():
    display = Display(4, 3)
    display.parse_and_execute("rect 3x2")

    assert display.pixels == [
        [True, True, True, False],
        [True, True, True, False],
        [False, False, False, False],
    ]


def test_shift_row():
    display = Display(4, 3)
    display.rect(3, 2)
    display.parse_and_execute("rotate row y=0 by 2")

    assert display.pixels == [
        [True, False, True, True],
        [True, True, True, False],
        [False, False, False, False],
    ]


def test_parse_shift_col():
    display = Display(4, 3)
    display.rect(3, 2)
    display.parse_and_execute("rotate column x=1 by 2")

    assert display.pixels == [
        [True, True, True, False],
        [True, False, True, False],
        [False, True, False, False],
    ]

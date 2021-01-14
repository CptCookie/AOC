from .solution import Lights, parse_line, OFF, ON, TOOGLE


def test_turning_lights():
    l = Lights()
    l.actuate([0, 0], [2, 2], ON)
    assert l.brightness == 9
    l.actuate([1, 1], [2, 2], TOOGLE)
    assert l.brightness == 5
    l.actuate([0, 0], [0, 0], OFF)
    assert l.brightness == 4


def test_turning_lights_bright():
    l = Lights(bin=False)
    l.actuate([0, 0], [0, 0], ON)
    assert l.brightness == 1
    l.actuate([0, 0], [999, 999], TOOGLE)
    assert l.brightness == 2000001


def test_parse():
    assert parse_line("toggle 173,401 through 496,407") == [
        [173, 401],
        [496, 407],
        TOOGLE,
    ]
    assert parse_line("turn on 313,306 through 363,621") == [[313, 306], [363, 621], ON]
    assert parse_line("turn off 61,44 through 567,111") == [[61, 44], [567, 111], OFF]

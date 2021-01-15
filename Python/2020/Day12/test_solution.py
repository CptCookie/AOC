from .solution import Ship


def test_turn():
    ship = Ship()
    ship.rotate(True, 90)
    assert ship.direction == "S"
    ship.rotate(True, 180)
    assert ship.direction == "N"
    ship.rotate(False, 90)
    assert ship.direction == "W"
    ship.rotate(False, 180)
    assert ship.direction == "E"


def test_manouver_normal():
    ship = Ship()
    ship.manouver("F10\nN3\nF7\nR90\nF11".split("\n"))
    assert ship.pos == (17, -8)
    assert ship.direction == "S"
    assert ship.distance == 25


def test_manouver_waypoint():
    ship = Ship(waypoint_nav=True)
    ship.manouver("F10\nN3\nF7\nR90\nF11".split("\n"))
    assert ship.pos == (214, -72)
    assert ship.way_pos == (4, -10)
    assert ship.distance == 286

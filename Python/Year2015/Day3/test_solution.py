from .solution import get_all_pos, get_unique, Position


def test_map_moves():
    assert get_all_pos("^>v<") == [
        Position(0, 0),
        Position(0, 1),
        Position(1, 1),
        Position(1, 0),
        Position(0, 0),
    ]


def test_unique():
    assert get_unique(get_all_pos("^v^v^v^v")) == [Position(0, 0), Position(0, 1)]

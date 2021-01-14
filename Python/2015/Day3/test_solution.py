from solution import map_moves, get_unique
def test_map_moves():
    assert map_moves('^>v<') == [[0,0], [0,1], [1,1], [1,0], [0,0]]

def test_unique():
    assert get_unique(map_moves('^v^v^v^v')) == [[0,0], [0,1]]
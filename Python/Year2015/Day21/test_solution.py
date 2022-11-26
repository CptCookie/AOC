from .solution import simulate_combat


def test_combat():
    assert simulate_combat([100, 1, 1], [100, 1, 1]) == True
    assert simulate_combat([100, 1, 1], [101, 1, 1]) == False
    assert simulate_combat([100, 1, 50], [101, 20, 1]) == False
    assert simulate_combat([100, 4, 0], [100, 8, 2]) == False
    assert simulate_combat([100, 4, 1], [100, 8, 2]) == False
    assert simulate_combat([8, 5, 5], [12, 7, 2]) == True

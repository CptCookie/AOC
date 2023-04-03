from .solution import location_at_dist


def test_slocation_at_dist():
    solution = location_at_dist((1, 1), 3, 10)
    assert solution == 6

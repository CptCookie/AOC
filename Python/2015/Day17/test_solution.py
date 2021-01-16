from .solution import get_all_valid_combination


def test_all_container():
    container = [20, 15, 10, 5, 5]
    combinations = get_all_valid_combination(container, 25)
    expected = [
        [15, 10],
        [20, 5],
        [20, 5],
        [15, 5, 5],
    ]
    assert sorted(combinations) == sorted(expected)

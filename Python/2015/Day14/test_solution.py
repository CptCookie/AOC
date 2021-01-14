from solution import positoning_after, score_after


def test_pos_after():
    reindeer = [["A", 14, 10, 127], ["B", 16, 11, 162]]
    assert positoning_after(reindeer, 1000) == {"A": 1120, "B": 1056}


def test_score_after():
    reindeer = [["A", 14, 10, 127], ["B", 16, 11, 162]]
    assert score_after(reindeer, 1000) == {"B": 689, "A": 312}

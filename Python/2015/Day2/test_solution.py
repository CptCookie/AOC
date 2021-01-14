from .solution import paper_needed, ribbon_needed


def test_wrapping_paper():
    assert paper_needed([2, 3, 4]) == 58
    assert paper_needed([1, 1, 10]) == 43


def test_ribbon():
    assert ribbon_needed([2, 3, 4]) == 34
    assert ribbon_needed([1, 1, 10]) == 14

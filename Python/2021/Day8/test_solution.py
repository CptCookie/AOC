from .solution import solution_2


def test_solution_2():
    test_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n"
    assert solution_2(test_input) == 5353


def test_solution_2_six_nine():
    test_input = "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb\n"
    assert solution_2(test_input) == 9361

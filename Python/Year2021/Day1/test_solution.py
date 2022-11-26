from .solution import solution_1, solution_2


def test_solution_1():
    test_input = """199
                    200
                    208
                    210
                    200
                    207
                    240
                    269
                    260
                    263"""
    assert solution_1(test_input) == 7


def test_solution_2():
    test_input = """199
                    200
                    208
                    210
                    200
                    207
                    240
                    269
                    260
                    263"""
    assert solution_2(test_input) == 5

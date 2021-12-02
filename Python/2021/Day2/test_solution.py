from .solution import solution_1, solution_2


def test_solution_1():
    test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
    assert solution_1(test_input) == -150


def test_solution_2():
    test_input = ""
    assert False

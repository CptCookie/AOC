from .solution import solution_1, solution_2


def test_solution_1():
    assert solution_1("ne,ne,ne") == 3
    assert solution_1("ne,ne,sw,sw") == 0
    assert solution_1("ne,ne,s,s") == 2
    assert solution_1("se,sw,se,sw,sw") == 3


def test_solution_2():
    assert solution_2("ne,ne,ne") == 3
    assert solution_2("ne,ne,sw,sw") == 2
    assert solution_2("ne,ne,s,s") == 2
    assert solution_2("se,se,sw,n") == 2

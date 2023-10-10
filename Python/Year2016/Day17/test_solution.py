from .solution import solution_1, solution_2


def test_solution_1():
    assert solution_1("ihgpwlah") == "DDRRRD"
    assert solution_1("kglvqrro") == "DDUDRLRRUDRD"
    assert solution_1("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"


def test_solution_2():
    assert solution_2("ihgpwlah") == 370
    assert solution_2("kglvqrro") == 492
    assert solution_2("ulqzkmiv") == 830

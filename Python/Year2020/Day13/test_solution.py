from .solution import valid_solution, soliution_2, solution_1


def test_solution2():
    p_in = "17,x,13,19"
    assert soliution_2(p_in) == 3417


def test_valid_solution():
    p_in = [17, -1, 13, 19]
    assert valid_solution(p_in, 3417)
    assert not valid_solution(p_in, 17)


def test_earlyest():
    solution = solution_1("939\n7,13,x,x,59,x,31,19".split("\n"))
    assert solution == 295

from .solution import solution_1, solution_2


def test_solution_1_example_1():
    test_input = "1122"
    assert solution_1(test_input) == 3


def test_solution_1_example_2():
    test_input = "1111"
    assert solution_1(test_input) == 4


def test_solution_1_example_3():
    test_input = "1234"
    assert solution_1(test_input) == 0


def test_solution_1_example_4():
    test_input = "91212129"
    assert solution_1(test_input) == 9


def test_solution_2_example_1():
    test_input = "1212"
    assert solution_2(test_input) == 6


def test_solution_2_example_2():
    test_input = "1221"
    assert solution_2(test_input) == 0


def test_solution_2_example_3():
    test_input = "123425"
    assert solution_2(test_input) == 4


def test_solution_2_example_4():
    test_input = "123123"
    assert solution_2(test_input) == 12


def test_solution_2_example_5():
    test_input = "12131415"
    assert solution_2(test_input) == 4

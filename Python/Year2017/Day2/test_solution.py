from .solution import solution_1, solution_2, get_divisables


def test_solution_1():
    test_input = "5\t1\t9\t5\n7\t5\t3\n2\t4\t6\t8\n"
    assert solution_1(test_input) == 18


def test_solution_2():
    test_input = "5\t9\t2\t8\n9\t4\t7\t3\n3\t8\t6\t5\n"
    assert solution_2(test_input) == 9


def test_get_divisibales_1():
    assert get_divisables([5, 9, 2, 8]) == (8, 2)


def test_get_divisibales_2():
    assert get_divisables([9, 4, 7, 3]) == (9, 3)


def test_get_divisibales_3():
    assert get_divisables([3, 8, 6, 5]) == (6, 3)

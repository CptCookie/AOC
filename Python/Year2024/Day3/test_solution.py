from .solution import solution_1, solution_2


def test_solution_1():
    TEST_INPUT = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert solution_1(TEST_INPUT) == 161


def test_solution_2():
    TEST_INPUT = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert solution_2(TEST_INPUT) == 48

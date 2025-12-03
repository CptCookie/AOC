from .solution import solution_1, solution_2, max_bank_joltage

TEST_INPUT = """987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_max_joltage():
    assert max_bank_joltage("98") == 98
    assert max_bank_joltage("987654321111111") == 98
    assert max_bank_joltage("987654321111111", digits=12) == 987654321111
    assert max_bank_joltage("234234234234278", digits=12) == 434234234278
    assert max_bank_joltage("818181911112111", digits=12) == 888911112111


def test_solution_1():
    assert solution_1(TEST_INPUT) == 357


def test_solution_2():
    assert solution_2(TEST_INPUT) == 3121910778619

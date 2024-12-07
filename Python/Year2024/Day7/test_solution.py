from .solution import solution_1, solution_2, parse_input, is_combination_of

TEST_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

TEST_DATA = [
    (190, (10, 19)),
    (3267, (81, 40, 27)),
    (83, (17, 5)),
    (156, (15, 6)),
    (7290, (6, 8, 6, 15)),
    (161011, (16, 10, 13)),
    (192, (17, 8, 14)),
    (21037, (9, 7, 18, 13)),
    (292, (11, 6, 16, 20)),
]


def test_combinations():
    assert is_combination_of(*TEST_DATA[0])
    assert is_combination_of(3267, (81, 40, 27))
    assert is_combination_of(292, (11, 6, 16, 20))


def test_concat_combinations():
    assert is_combination_of(11, (1, 1), True)
    assert is_combination_of(2691, (9, 260, 1), True)
    assert is_combination_of(156, (15, 6), True)
    assert is_combination_of(7290, (6, 8, 6, 15), True)
    assert is_combination_of(192, (17, 8, 14), True)
    assert is_combination_of(815, (8, 15), True)
    assert is_combination_of(51, (2, 3, 1), True)


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 3749


def test_solution_2():
    assert solution_2(TEST_INPUT) == 11387

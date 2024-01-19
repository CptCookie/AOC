from .solution import (
    solution_1,
    solution_2,
    parse_input,
    number_of_solutions,
    number_of_expanded_solutions,
)

TEST_INPUT = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

TEST_DATA = [
    ("???.###", (1, 1, 3)),
    (".??..??...?##.", (1, 1, 3)),
    ("?#?#?#?#?#?#?#?", (1, 3, 1, 6)),
    ("????.#...#...", (4, 1, 1)),
    ("????.######..#####.", (1, 6, 5)),
    ("?###????????", (3, 2, 1)),
]


def test_number_solutions_terminations():
    assert number_of_solutions("", ()) == 1
    assert number_of_solutions("???", ())
    assert number_of_solutions(".?.", ())
    assert number_of_solutions("", (1,)) == 0
    assert number_of_solutions("#", ()) == 0
    assert number_of_solutions("#...##", (2, 2)) == 0
    assert number_of_solutions("#", (2,)) == 0


def test_number_of_solutions():
    assert number_of_solutions("???.###", (1, 1, 3)) == 1
    assert number_of_solutions(".??..??...?##.", (1, 1, 3)) == 4
    assert number_of_solutions("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert number_of_solutions("????.#...#...", (4, 1, 1)) == 1
    assert number_of_solutions("????.######..#####.", (1, 6, 5)) == 4
    assert number_of_solutions("?###????????", (3, 2, 1)) == 10


def test_number_of_solutions_expanded():
    assert number_of_expanded_solutions("???.###", (1, 1, 3)) == 1
    assert number_of_expanded_solutions(".??..??...?##.", (1, 1, 3)) == 16384
    assert number_of_expanded_solutions("?#?#?#?#?#?#?#?", (1, 3, 1, 6)) == 1
    assert number_of_expanded_solutions("????.#...#...", (4, 1, 1)) == 16
    assert number_of_expanded_solutions("????.######..#####.", (1, 6, 5)) == 2500
    assert number_of_expanded_solutions("?###????????", (3, 2, 1)) == 506250


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 21


def test_solution_2():
    assert solution_2(TEST_INPUT) == 525152

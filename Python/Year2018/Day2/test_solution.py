from .solution import solution_1, solution_2, parse_input, contains_multiples, common_id

TEST_INPUT = """abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab
"""

TEST_DATA = [
    "abcdef",
    "bababc",
    "abbcde",
    "abcccd",
    "aabcdd",
    "abcdee",
    "ababab",
]
TEST_DATA_COMMON = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_contains_multi():
    assert contains_multiples("abcdef", 2) == False
    assert contains_multiples("abcdef", 3) == False
    assert contains_multiples("bababc", 2) == True
    assert contains_multiples("bababc", 3) == True
    assert contains_multiples("abbcde", 2) == True
    assert contains_multiples("abbcde", 3) == False


def test_common_id():
    assert common_id(TEST_DATA_COMMON) == "fgij"


def test_solution_1():
    assert solution_1(TEST_INPUT) == 12


def test_solution_2():
    assert solution_2(TEST_INPUT)

from .solution import solution_1, solution_2, reduce_bitlist, most_common_bits

test_data = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]
test_input = """00100\n11110\n10110\n10111\n10101\n01111\n00111\n11100\n10000\n11001\n00010\n01010"""


def test_common_bitlist():
    assert most_common_bits(["11111", "00000"]) == "11111"
    assert most_common_bits(["11111", "00000"], inverse=True) == "00000"
    assert most_common_bits(test_data) == "10110"
    assert most_common_bits(test_data, inverse=True) == "01001"


def test_reduced_bitlist():
    assert reduce_bitlist(test_data) == "10111"


def test_reduced_bitlist_least_common():
    assert reduce_bitlist(test_data, least_common=True) == "01010"


def test_solution_1():
    assert solution_1(test_input) == 198


def test_solution_2():
    assert solution_2(test_input) == 230

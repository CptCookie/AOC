from .solution import parse_part_1, parse_part_2, solution_1, solution_2

TEST_INPUT = """123 328  51 64 \n 45 64  387 23 \n  6 98  215 314\n*   +   *   +  """

TEST_DATA_PART_1 = [
    ["123", "45", "6", "*"],
    ["328", "64", "98", "+"],
    ["51", "387", "215", "*"],
    ["64", "23", "314", "+"],
]


TEST_DATA_PART_2 = [
    ["356", "24", "1", "*"],
    ["8", "248", "369", "+"],
    ["175", "581", "32", "*"],
    ["4", "431", "623", "+"],
]


def test_parsing_part_1():
    assert parse_part_1(TEST_INPUT) == TEST_DATA_PART_1


def test_parsing_part_2():
    result = parse_part_2(TEST_INPUT)
    assert result == TEST_DATA_PART_2


def test_solution_1():
    assert solution_1(TEST_INPUT) == 4277556


def test_solution_2():
    assert solution_2(TEST_INPUT) == 3263827

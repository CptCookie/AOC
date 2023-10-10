from .solution import solution_1, solution_2, checksum, inflate_dragon

TEST_INPUT = """
"""

TEST_DATA = []


def test_checksum():
    assert checksum("110010110100") == "100"
    assert checksum("10000011110010000111") == "01100"


def test_dragon():
    assert inflate_dragon("1", 3) == "100"
    assert inflate_dragon("0", 3) == "001"
    assert inflate_dragon("11111", 11) == "11111000000"
    assert inflate_dragon("111100001010", 25) == "1111000010100101011110000"
    assert inflate_dragon("10000", 20) == "10000011110010000111"


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT)

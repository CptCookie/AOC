from .solution import solution_1, solution_2

TEST_SIMPLE = """
..X...
.SAMX.
.A..A.
XMAS.S
.X....
"""


TEST_INPUT = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

TEST_MAS = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""


def test_solution_1():
    assert solution_1(TEST_SIMPLE) == 4
    assert solution_1(TEST_INPUT) == 18


def test_solution_2():
    assert solution_2(TEST_MAS) == 9

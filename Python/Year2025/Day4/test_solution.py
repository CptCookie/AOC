from .solution import solution_1, solution_2

TEST_INPUT = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_solution_1():
    assert solution_1(TEST_INPUT) == 13


def test_solution_2():
    assert solution_2(TEST_INPUT)

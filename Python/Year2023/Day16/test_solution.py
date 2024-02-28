from .solution import solution_1, solution_2, get_num_energized

TEST_INPUT = """
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""


def test_solution_1():
    assert solution_1(TEST_INPUT) == 46


def test_solution_2():
    assert solution_2(TEST_INPUT) == 51

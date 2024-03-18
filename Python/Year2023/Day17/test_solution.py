from .solution import solution_1, solution_2, parse_input

TEST_INPUT = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""


def test_solution_1():
    assert solution_1("11\n21\n") == 2
    assert solution_1("111\n221\n331") == 4
    assert solution_1("11111\n22221\n33331\n") == 7
    assert solution_1(TEST_INPUT) == 102


def test_solution_2():
    assert solution_2(TEST_INPUT) == 94

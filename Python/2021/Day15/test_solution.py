from .solution import solution_1, solution_2, get_next_node

TEST_INPUT = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


def test_next():
    assert get_next_node([((1, 0), 2), ((0, 1), 3)]) == ((1, 0), 2)


def test_solution_mini():
    assert solution_1("""123\n234\n456""") == 15


def test_solution_1():
    assert solution_1(TEST_INPUT) == 40


def test_solution_2():
    assert solution_2(TEST_INPUT) == 315

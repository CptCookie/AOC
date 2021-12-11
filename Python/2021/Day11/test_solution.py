from .solution import parse_data, solution_1, solution_2, DumboFishSwarm

TEST_DATA = """
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def test_adjacent_corner():
    swarm = DumboFishSwarm(parse_data(TEST_DATA))
    adj = swarm.get_adjacent_points(0, 0)
    for n in [(0, 1), (1, 1), (1, 0)]:
        assert n in adj


def test_adjacent_center():
    swarm = DumboFishSwarm(parse_data(TEST_DATA))
    adj = swarm.get_adjacent_points(2, 2)
    for n in [(2, 1), (1, 2), (1, 1), (2, 3), (3, 2), (3, 3), (1, 3), (3, 1)]:
        assert n in adj


def test_adjacent_center():
    swarm = DumboFishSwarm(parse_data("000\n000\n000"))
    swarm.add_1()
    assert swarm.swarm == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def test_flash_easy():
    swarm = DumboFishSwarm(parse_data("000\n090\n000"))
    assert swarm.step() == 1
    assert swarm.swarm == [[2, 2, 2], [2, 0, 2], [2, 2, 2]]


def test_flash_combo():
    swarm = DumboFishSwarm(parse_data("11111\n19991\n19191\n19991\n11111"))
    swarm.step()

    assert swarm.swarm == [
        [3, 4, 5, 4, 3],
        [4, 0, 0, 0, 4],
        [5, 0, 0, 0, 5],
        [4, 0, 0, 0, 4],
        [3, 4, 5, 4, 3],
    ]


def test_solution_1():
    assert solution_1(TEST_DATA) == 1656


def test_solution_2():
    assert solution_2(TEST_DATA) == 195

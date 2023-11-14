from .solution import solution_1, solution_2, parse_input, run_amps, run_amps_loop

TEST_INPUT = """
"""

TEST_DATA = []


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_amps_run():
    assert (
        run_amps(
            [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0],
            [4, 3, 2, 1, 0],
        )
        == 43210
    )

    assert (
        # fmt:off
        run_amps(
            [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0],
            [0, 1, 2, 3, 4],
        )
        == 54321
    )
    assert (
        run_amps(
            # fmt:off
        [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0],
        [1, 0, 4, 3, 2],
        )
        == 65210
    )


def test_amps_loop_run():
    assert (
        run_amps_loop(
            # fmt: off
        [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5],
        [9,8,7,6,5]
        )
        == 139629729
    )


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT)

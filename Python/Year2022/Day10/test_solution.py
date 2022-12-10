from .solution import (
    get_cycle_signal,
    parse_data,
    solution_1,
    solution_2,
    calc_timeline,
)

TEST_INPUT_SMALL = """noop
addx 3
addx -5"""

TEST_DATA_SMALL = [
    ["noop"],
    ["addx", "3"],
    ["addx", "-5"],
]


def test_parse_data():
    assert parse_data(TEST_INPUT_SMALL) == TEST_DATA_SMALL


def test_timeline():
    expected = [1, 1, 1, 4, 4, -1]
    assert calc_timeline(TEST_DATA_SMALL) == expected


def test_timelinebig():
    data = parse_data(TEST_INPUT_BIG)
    timeline = calc_timeline(data)

    assert get_cycle_signal(timeline, 20) == 420
    assert get_cycle_signal(timeline, 60) == 1140
    assert get_cycle_signal(timeline, 100) == 1800
    assert get_cycle_signal(timeline, 140) == 2940
    assert get_cycle_signal(timeline, 180) == 2880
    assert get_cycle_signal(timeline, 220) == 3960


def test_solution_1():
    assert solution_1(TEST_INPUT_BIG) == 13140


def test_solution_2():
    expected = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....""".replace(
        ".", " "
    )
    display = solution_2(TEST_INPUT_BIG)
    print(display)
    for line in range(6):
        assert display.splitlines()[line] == expected.splitlines()[line]


TEST_INPUT_BIG = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

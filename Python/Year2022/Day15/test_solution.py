from .solution import (
    solution_1,
    solution_2,
    parse_input,
    get_sensor_line,
    get_covered_line,
    get_sensor_line_ranges,
    get_sensor_range,
    get_sensor_fring,
)

TEST_INPUT = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""

TEST_DATA = [
    [2, 18, -2, 15],
    [9, 16, 10, 16],
    [13, 2, 15, 3],
    [12, 14, 10, 16],
    [10, 20, 10, 16],
    [14, 17, 10, 16],
    [8, 7, 2, 10],
    [2, 0, 2, 10],
    [0, 11, 2, 10],
    [20, 14, 25, 17],
    [17, 20, 21, 22],
    [16, 7, 15, 3],
    [14, 3, 15, 3],
    [20, 1, 15, 3],
]


def test_sensor_line():
    assert get_sensor_line([0, 11, 2, 10], 10) == [-2, -1, 0, 1, 2]
    assert get_sensor_line([8, 7, 2, 10], 0) == [6, 7, 8, 9, 10]
    assert get_sensor_line([8, 7, 2, 10], -1) == [7, 8, 9]
    assert get_sensor_line([8, 7, 2, 10], -2) == [8]
    assert get_sensor_line([8, 7, 2, 10], 16) == [8]
    assert get_sensor_line([8, 7, 2, 10], 14) == [6, 7, 8, 9, 10]
    assert get_sensor_line([8, 7, 2, 10], 10) == [
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
    ]


def test_sensor_line_range():
    srange = get_sensor_range([[8, 7, 2, 10]])
    assert get_sensor_line_ranges(*srange[0], -2) == (8, 8)
    assert get_sensor_line_ranges(*srange[0], -1) == (7, 9)
    assert get_sensor_line_ranges(*srange[0], 0) == (6, 10)
    assert get_sensor_line_ranges(*srange[0], 10) == (2, 14)
    assert get_sensor_line_ranges(*srange[0], 14) == (6, 10)


def test_get_sensor_fring():
    expected = [
        (4, 0),
        (3, 1),
        (5, 1),
        (2, 2),
        (6, 2),
        (1, 3),
        (7, 3),
        (0, 4),
        (8, 4),
        (1, 5),
        (7, 5),
        (2, 6),
        (6, 6),
        (3, 7),
        (5, 7),
        (4, 8),
    ]
    result = get_sensor_fring(4, 4, 3)
    for exp in expected:
        assert exp in result
    assert len(result) == len(expected)


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_coverage_line():
    result = get_covered_line(TEST_DATA, 10)
    assert len(result) == 26
    for n in range(-1, 25):
        assert n in result or n == 2


    """
       o
      o.o
     o...o
    o..x..o
     o...o
      o.o
       o
    """
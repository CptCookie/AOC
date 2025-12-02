from .solution import (
    solution_1,
    solution_2,
    parse_input,
    get_matching_ids,
    PATTERN_SOLUTION_1,
    PATTERN_SOLUTION_2,
)

TEST_INPUT = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

TEST_DATA = [
    range(11, 23),
    range(95, 116),
    range(998, 1013),
    range(1188511880, 1188511891),
    range(222220, 222225),
    range(1698522, 1698529),
    range(446443, 446450),
    range(38593856, 38593863),
    range(565653, 565660),
    range(824824821, 824824828),
    range(2121212118, 2121212125),
]

TEST_CASES = [
    (range(11, 23), [11, 22], [11, 22]),
    (range(95, 116), [99], [99, 111]),
    (range(998, 1013), [1010], [999, 1010]),
    (range(1188511880, 1188511891), [1188511885], [1188511885]),
    (range(222220, 222225), [222222], [222222]),
    (range(1698522, 1698529), [], []),
    (range(446443, 446450), [446446], [446446]),
    (range(38593856, 38593863), [38593859], [38593859]),
    (range(565653, 565660), [], [565656]),
    (range(824824821, 824824828), [], [824824824]),
    (range(2121212118, 2121212125), [], [2121212121]),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_valid_matching_pattern_1():
    for range, expected, _ in TEST_CASES:
        assert get_matching_ids(range, PATTERN_SOLUTION_1) == expected


def test_valid_matching_pattern_2():
    for range, _, expected in TEST_CASES:
        assert get_matching_ids(range, PATTERN_SOLUTION_2) == expected


def test_solution_1():
    assert solution_1(TEST_INPUT) == 1227775554


def test_solution_2():
    assert solution_2(TEST_INPUT) == 4174379265

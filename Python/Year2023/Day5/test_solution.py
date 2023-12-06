from .solution import (
    solution_1,
    solution_2,
    parse_input,
    map_value_by_section,
    map_value_by_alma,
)

TEST_INPUT = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

TEST_SEEDS = [79, 14, 55, 13]
TEST_MAPS = [
    [(50, 98, 2), (52, 50, 48)],
    [(0, 15, 37), (37, 52, 2), (39, 0, 15)],
    [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)],
    [(88, 18, 7), (18, 25, 70)],
    [(45, 77, 23), (81, 45, 19), (68, 64, 13)],
    [(0, 69, 1), (1, 0, 69)],
    [(60, 56, 37), (56, 93, 4)],
]


def test_map_section():
    section = [(50, 98, 2), (52, 50, 48)]
    assert map_value_by_section(48, section) == 48
    assert map_value_by_section(50, section) == 52
    assert map_value_by_section(51, section) == 53
    assert map_value_by_section(97, section) == 99
    assert map_value_by_section(98, section) == 50
    assert map_value_by_section(99, section) == 51

    assert map_value_by_section(79, section) == 81
    assert map_value_by_section(14, section) == 14
    assert map_value_by_section(55, section) == 57
    assert map_value_by_section(13, section) == 13


def test_map_alma():
    assert map_value_by_alma(79, TEST_MAPS) == 82
    assert map_value_by_alma(14, TEST_MAPS) == 43
    assert map_value_by_alma(55, TEST_MAPS) == 86
    assert map_value_by_alma(13, TEST_MAPS) == 35


def test_parsing():
    assert parse_input(TEST_INPUT) == (TEST_SEEDS, TEST_MAPS)


def test_solution_1():
    assert solution_1(TEST_INPUT) == 35


def test_solution_2():
    assert solution_2(TEST_INPUT) == 46

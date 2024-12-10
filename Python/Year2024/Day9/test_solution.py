from .solution import (
    solution_1,
    solution_2,
    parse_input,
    defrag_sectors,
    calculate_checksum,
    defrag_blocks,
)

TEST_INPUT = """2333133121414131402
"""

TEST_DATA = [
    (0, 2),
    (None, 3),
    (1, 3),
    (None, 3),
    (2, 1),
    (None, 3),
    (3, 3),
    (None, 1),
    (4, 2),
    (None, 1),
    (5, 4),
    (None, 1),
    (6, 4),
    (None, 1),
    (7, 3),
    (None, 1),
    (8, 4),
    (9, 2),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_defrag_sectors_simple():
    test_blocks = [("0", 1), (None, 2), ("1", 3), (None, 3), ("2", 5)]
    expected = [("0", 1), ("2", 2), ("1", 3), ("2", 3)]
    assert defrag_sectors(test_blocks) == expected


def test_defrag_sectors_complex():
    expected = [
        (0, 2),
        (9, 2),
        (8, 1),
        (1, 3),
        (8, 3),
        (2, 1),
        (7, 3),
        (3, 3),
        (6, 1),
        (4, 2),
        (6, 1),
        (5, 4),
        (6, 2),
    ]
    assert defrag_sectors(TEST_DATA) == expected


def test_checksum_simple():
    assert calculate_checksum([(0, 1), (2, 2), (1, 3), (2, 3)]) == 10


def test_checksum_complex():
    test_data = [
        (0, 2),
        (9, 2),
        (8, 1),
        (1, 3),
        (8, 3),
        (2, 1),
        (7, 3),
        (3, 3),
        (6, 1),
        (4, 2),
        (6, 1),
        (5, 4),
        (6, 2),
    ]
    assert calculate_checksum(test_data) == 1928


def test_defrag_blocks():
    expected = [
        (0, 2),
        (9, 2),
        (2, 1),
        (1, 3),
        (7, 3),
        (None, 1),
        (4, 2),
        (None, 1),
        (3, 3),
        # empty blocks get fragmented but it does not matter
        (None, 1),
        (None, 2),
        (None, 1),
        (5, 4),
        (None, 1),
        (6, 4),
        (None, 1),
        (None, 3),
        (None, 1),
        (8, 4),
        (None, 2),
    ]
    assert defrag_blocks(TEST_DATA) == expected


def test_solution_1():
    assert solution_1(TEST_INPUT) == 1928


def test_solution_2():
    assert solution_2(TEST_INPUT) == 2858

from .solution import *

TEST_INPUT = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


def test_count_cicle_1():
    polymer = TEST_INPUT.splitlines()[0]
    patterns = parse_patterns(TEST_INPUT)
    elem_count = count_for_cicle(polymer, patterns, 1)

    assert elem_count == Counter("NCNBCHB")


def test_count_cicle_2():
    polymer = TEST_INPUT.splitlines()[0]
    patterns = parse_patterns(TEST_INPUT)
    elem_count = count_for_cicle(polymer, patterns, 2)

    assert elem_count == Counter("NBCCNBBBCBHCB")


def test_count_cicle_3():
    polymer = TEST_INPUT.splitlines()[0]
    patterns = parse_patterns(TEST_INPUT)
    elem_count = count_for_cicle(polymer, patterns, 3)

    assert elem_count == Counter("NBBBCNCCNBBNBNBBCHBHHBCHB")


def test_solution_1():
    assert solution_1(TEST_INPUT) == 1588


def test_solution_2():
    assert solution_2(TEST_INPUT) == 2188189693529

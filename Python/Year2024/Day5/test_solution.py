from .solution import (
    solution_1,
    solution_2,
    parse_rules,
    parse_updates,
    in_correct_order,
    fix_ordering,
)

TEST_INPUT = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""

TEST_UPDATES = [
    [75, 47, 61, 53, 29],
    [97, 61, 53, 29, 13],
    [75, 29, 13],
    [75, 97, 47, 61, 53],
    [61, 13, 29],
    [97, 13, 75, 29, 47],
]

TEST_RULES = {
    29: {13},
    47: {53, 13, 61, 29},
    53: {29, 13},
    61: {13, 53, 29},
    75: {29, 53, 47, 61, 13},
    97: {13, 61, 47, 29, 53, 75},
}


def test_parsing_rules():
    assert parse_rules(TEST_INPUT) == TEST_RULES


def test_parsing_updates():
    assert parse_updates(TEST_INPUT) == TEST_UPDATES


def test_in_correct_order():
    assert in_correct_order(TEST_UPDATES[0], TEST_RULES)
    assert in_correct_order(TEST_UPDATES[1], TEST_RULES)
    assert in_correct_order(TEST_UPDATES[2], TEST_RULES)
    assert not in_correct_order(TEST_UPDATES[3], TEST_RULES)
    assert not in_correct_order(TEST_UPDATES[4], TEST_RULES)
    assert not in_correct_order(TEST_UPDATES[5], TEST_RULES)


def test_fix_ordering():
    assert fix_ordering(TEST_UPDATES[3], TEST_RULES) == [97, 75, 47, 61, 53]
    assert fix_ordering(TEST_UPDATES[4], TEST_RULES) == [61, 29, 13]
    assert fix_ordering(TEST_UPDATES[5], TEST_RULES) == [97, 75, 47, 29, 13]


def test_solution_1():
    assert solution_1(TEST_INPUT) == 143


def test_solution_2():
    assert solution_2(TEST_INPUT) == 123

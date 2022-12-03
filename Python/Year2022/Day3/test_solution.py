from .solution import (
    solution_1,
    solution_2,
    get_priority,
    find_wrong_item,
    find_auth_badge,
)

TEST_DATA = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_get_prio():
    assert get_priority("p") == 16
    assert get_priority("L") == 38
    assert get_priority("P") == 42
    assert get_priority("v") == 22
    assert get_priority("t") == 20
    assert get_priority("s") == 19


def test_wrong_item():
    assert find_wrong_item("vJrwpWtwJgWrhcsFMMfFFhFp") == "p"
    assert find_wrong_item("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL") == "L"
    assert find_wrong_item("PmmdzqPrVvPwwTWBwg") == "P"
    assert find_wrong_item("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn") == "v"
    assert find_wrong_item("ttgJtRGJQctTZtZT") == "t"
    assert find_wrong_item("CrZsJsPPZsGzwwsLwLmpwMDw") == "s"


def test_solution_1():
    assert solution_1(TEST_DATA) == 157


def test_auth_badge():
    assert (
        find_auth_badge(
            [
                "vJrwpWtwJgWrhcsFMMfFFhFp",
                "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
                "PmmdzqPrVvPwwTWBwg",
            ]
        )
        == "r"
    )

    assert (
        find_auth_badge(
            [
                "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
                "ttgJtRGJQctTZtZT",
                "CrZsJsPPZsGzwwsLwLmpwMDw",
            ]
        )
        == "Z"
    )


def test_solution_2():
    assert solution_2(TEST_DATA) == 70

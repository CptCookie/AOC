from .solution import solution_1, solution_2, parse_input, hash_acsii

TEST_INPUT = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

TEST_DATA = [
    "rn=1",
    "cm-",
    "qp=3",
    "cm=2",
    "qp-",
    "pc=4",
    "ot=9",
    "ab=5",
    "pc-",
    "pc=6",
    "ot=7",
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_hash():
    assert hash_acsii("HASH") == 52
    assert hash_acsii("rn=1") == 30
    assert hash_acsii("cm-") == 253


def test_solution_1():
    assert solution_1(TEST_INPUT) == 1320


def test_solution_2():
    assert solution_2(TEST_INPUT) == 145

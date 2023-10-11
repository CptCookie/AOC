from .solution import (
    rotate,
    rotate_letter,
    reverse,
    move,
    swap_pos,
    swap_letter,
    reverse_rotate_letter,
    solution_1,
    solution_2,
)


TEST_INPUT = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
"""


def test_swap_pos():
    assert swap_pos(list("abcde"), 4, 0) == list("ebcda")
    assert swap_pos(list("ebcda"), 4, 0) == list("abcde")


def test_swap_letter():
    assert swap_letter(list("ebcda"), "d", "b") == list("edcba")
    assert swap_letter(list("edcba"), "d", "b") == list("ebcda")


def test_rotate():
    assert rotate(list("abcde"), 1) == list("bcdea")
    assert rotate(list("abcde"), -1) == list("eabcd")

    assert rotate(list("bcdea"), -1) == list("abcde")
    assert rotate(list("eabcd"), 1) == list("abcde")


def test_rotate_letter():
    assert rotate_letter(list("abdec"), "b") == list("ecabd")
    assert rotate_letter(list("ecabd"), "d") == list("decab")


def test_reverse_rotate_letter():
    assert reverse_rotate_letter(list("ecabd"), "b") == list("abdec")
    assert reverse_rotate_letter(list("decab"), "d") == list("ecabd")


def test_reverse():
    assert reverse(list("abcde"), 0, 2) == list("cbade")
    assert reverse(list("abcde"), 2, 4) == list("abedc")
    assert reverse(list("abcde"), 1, 2) == list("acbde")

    assert reverse(list("cbade"), 0, 2) == list("abcde")
    assert reverse(list("abedc"), 2, 4) == list("abcde")
    assert reverse(list("acbde"), 1, 2) == list("abcde")


def test_move():
    assert move(list("bcdea"), 1, 4) == list("bdeac")
    assert move(list("bdeac"), 3, 0) == list("abdec")

    assert move(list("bdeac"), 4, 1) == list("bcdea")
    assert move(list("abdec"), 0, 3) == list("bdeac")


def test_solution_1():
    assert solution_1(TEST_INPUT, seed="abcde") == "decab"


def test_solution_2():
    assert solution_2(TEST_INPUT, seed="decab") == "abcde"

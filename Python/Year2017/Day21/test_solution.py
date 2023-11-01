from .solution import (
    solution_1,
    solution_2,
    flip_hor,
    flip_vertical,
    rotate_clock,
    disassemble_display,
    reassemble_display,
)


def test_flip_hor():
    assert flip_hor(("..#", ".##", "#..")) == ("#..", "##.", "..#")
    assert flip_hor(("..##", ".#.#", "#..#")) == ("##..", "#.#.", "#..#")


def test_flip_vertical():
    assert flip_vertical(("..#", ".##", "#..")) == ("#..", ".##", "..#")
    assert flip_vertical(("..##", ".#.#", "#..#")) == ("#..#", ".#.#", "..##")


def test_rotate():
    assert rotate_clock(("..#", ".##", "#.."), 1) == ("#..", ".#.", ".##")
    assert rotate_clock(("#..", ".#.", ".##"), 1) == ("..#", "##.", "#..")
    assert rotate_clock(("..#", ".##", "#.."), 2) == ("..#", "##.", "#..")
    assert rotate_clock(("..#", ".##", "#.."), 4) == ("..#", ".##", "#..")


def test_disassemble_display():
    assert disassemble_display(["1234", "5678", "9012", "3456"]) == [
        ("12", "56"),
        ("34", "78"),
        ("90", "34"),
        ("12", "56"),
    ]
    assert disassemble_display(
        [
            "abcdefghi",
            "jklmnopqr",
            "stuvwxyz0",
            "123456789",
            "abcdefghi",
            "jklmnopqr",
            "stuvwxyz0",
            "123456789",
            "abcdefghi",
        ]
    ) == [
        ("abc", "jkl", "stu"),
        ("def", "mno", "vwx"),
        ("ghi", "pqr", "yz0"),
        ("123", "abc", "jkl"),
        ("456", "def", "mno"),
        ("789", "ghi", "pqr"),
        ("stu", "123", "abc"),
        ("vwx", "456", "def"),
        ("yz0", "789", "ghi"),
    ]


def test_reassemble():
    assert reassemble_display(
        [("12", "56"), ("34", "78"), ("90", "34"), ("12", "56")]
    ) == ["1234", "5678", "9012", "3456"]

    assert reassemble_display(
        [
            ("abc", "jkl", "stu"),
            ("def", "mno", "vwx"),
            ("ghi", "pqr", "yz0"),
            ("123", "abc", "jkl"),
            ("456", "def", "mno"),
            ("789", "ghi", "pqr"),
            ("stu", "123", "abc"),
            ("vwx", "456", "def"),
            ("yz0", "789", "ghi"),
        ]
    ) == [
        "abcdefghi",
        "jklmnopqr",
        "stuvwxyz0",
        "123456789",
        "abcdefghi",
        "jklmnopqr",
        "stuvwxyz0",
        "123456789",
        "abcdefghi",
    ]


def test_solution_1():
    assert solution_1(TEST_INPUT)


def test_solution_2():
    assert solution_2(TEST_INPUT)

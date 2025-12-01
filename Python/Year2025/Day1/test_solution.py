from .solution import solution_1, solution_2, parse_input, Dial

TEST_INPUT = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

TEST_DATA = [
    ("L", 68),
    ("L", 30),
    ("R", 48),
    ("L", 5),
    ("R", 60),
    ("L", 55),
    ("L", 1),
    ("L", 99),
    ("R", 14),
    ("L", 82),
]


def test_turn_right_to_0():
    dial = Dial()
    dial.number = 80
    dial.turn("R", 20)

    assert dial.number == 0
    assert dial.zero_pass_cnt == 0
    assert dial.zero_cnt == 1


def test_turn_right_multi_to_0():
    dial = Dial()
    dial.number = 80
    dial.turn("R", 220)

    assert dial.number == 0
    assert dial.zero_pass_cnt == 2
    assert dial.zero_cnt == 1


def test_turn_right_over_0():
    dial = Dial()
    dial.number = 80
    dial.turn("R", 21)

    assert dial.number == 1
    assert dial.zero_pass_cnt == 1
    assert dial.zero_cnt == 0


def test_turn_right_of_0():
    dial = Dial()
    dial.number = 0
    dial.turn("R", 1)

    assert dial.number == 1
    assert dial.zero_pass_cnt == 0
    assert dial.zero_cnt == 0


def test_turn_left_to_0():
    dial = Dial()
    dial.number = 20
    dial.turn("L", 20)

    assert dial.number == 0
    assert dial.zero_pass_cnt == 0
    assert dial.zero_cnt == 1


def test_turn_left_over_0():
    dial = Dial()
    dial.number = 20
    dial.turn("L", 21)

    assert dial.number == 99
    assert dial.zero_pass_cnt == 1
    assert dial.zero_cnt == 0


def test_turn_left_of_0():
    dial = Dial()
    dial.number = 0
    dial.turn("L", 1)

    assert dial.number == 99
    assert dial.zero_pass_cnt == 0
    assert dial.zero_cnt == 0


def test_left_multi_on_0():
    dial = Dial()
    dial.number = 10
    dial.turn("L", 210)

    assert dial.number == 0
    assert dial.zero_cnt == 1
    assert dial.zero_pass_cnt == 2


def test_mulit_rotation_R():
    dial = Dial()
    dial.number = 50
    dial.turn("R", 1000)
    assert dial.zero_pass_cnt == 10
    assert dial.number == 50


def test_mulit_rotation_L():
    dial = Dial()
    dial.number = 50
    dial.turn("L", 1000)
    assert dial.zero_pass_cnt == 10
    assert dial.number == 50


def test_turn():
    dial = Dial()

    dial.turn(*TEST_DATA[0])
    assert dial.number == 82
    assert dial.zero_pass_cnt == 1
    assert dial.zero_cnt == 0

    dial.turn(*TEST_DATA[1])
    assert dial.number == 52
    assert dial.zero_pass_cnt == 1
    assert dial.zero_cnt == 0

    dial.turn(*TEST_DATA[2])
    assert dial.number == 0
    assert dial.zero_pass_cnt == 1
    assert dial.zero_cnt == 1

    dial.turn(*TEST_DATA[3])
    assert dial.number == 95
    assert dial.zero_pass_cnt == 1
    assert dial.zero_cnt == 1

    dial.turn(*TEST_DATA[4])
    assert dial.number == 55
    assert dial.zero_pass_cnt == 2
    assert dial.zero_cnt == 1

    dial.turn(*TEST_DATA[5])
    assert dial.number == 0
    assert dial.zero_pass_cnt == 2
    assert dial.zero_cnt == 2

    dial.turn(*TEST_DATA[6])
    assert dial.number == 99
    assert dial.zero_pass_cnt == 2
    assert dial.zero_cnt == 2

    dial.turn(*TEST_DATA[7])
    assert dial.number == 0
    assert dial.zero_pass_cnt == 2
    assert dial.zero_cnt == 3

    dial.turn(*TEST_DATA[8])
    assert dial.number == 14
    assert dial.zero_pass_cnt == 2
    assert dial.zero_cnt == 3

    dial.turn(*TEST_DATA[9])
    assert dial.number == 32
    assert dial.zero_pass_cnt == 3
    assert dial.zero_cnt == 3


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_solution_1():
    assert solution_1(TEST_INPUT) == 3


def test_solution_2():
    assert solution_2(TEST_INPUT) == 6

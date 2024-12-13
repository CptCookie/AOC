from .solution import solution_1, solution_2, parse_input, solve_equation

TEST_INPUT = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""

TEST_DATA = [
    (94, 34, 22, 67, 8400, 5400),
    (26, 66, 67, 21, 12748, 12176),
    (17, 86, 84, 37, 7870, 6450),
    (69, 23, 27, 71, 18641, 10279),
]


def test_parsing():
    assert parse_input(TEST_INPUT) == TEST_DATA


def test_equation_solution():
    assert solve_equation(TEST_DATA[0]) == (80, 40)
    assert solve_equation(TEST_DATA[1]) is None
    assert solve_equation(TEST_DATA[2]) == (38, 86)
    assert solve_equation(TEST_DATA[3]) is None


def test_solution_1():
    assert solution_1(TEST_INPUT) == 480


def test_solution_2():
    assert solution_2(TEST_INPUT)

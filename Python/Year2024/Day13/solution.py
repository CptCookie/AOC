import re


Equation = tuple[int, int, int, int, int, int]


def parse_input(aoc_input: str) -> list[Equation]:
    pattern = re.compile(
        r"X\+(\d+).*Y\+(\d+)\n.*X\+(\d+).*Y\+(\d+)\n.*X=(\d+).*Y=(\d+)"
    )
    return [tuple(map(int, m.groups())) for m in pattern.finditer(aoc_input)]


def solve_equation(equation: Equation, offset=0) -> tuple[int, int] | None:
    """
    x = n * a1 + m * b1
    y = n * a2 + m * b2
    """
    try:
        a1, a2, b1, b2, x, y = equation

        if offset != 0:
            x, y = x + offset, y + offset

        n = (b1 * y - b2 * x) / (a2 * b1 - a1 * b2)
        m = (a1 * y - a2 * x) / (a1 * b2 - a2 * b1)

        if n % 1 != 0 or m % 1 != 0:
            return None

        return int(n), int(m)

    except ZeroDivisionError:
        return None


def token_to_win(equation: Equation, offset=0) -> int | None:
    if solve := solve_equation(equation, offset):
        return solve[0] * 3 + solve[1] * 1
    else:
        return 0


def solution_1(aoc_input: str):
    equations = parse_input(aoc_input)
    return sum(token_to_win(eq) for eq in equations)


def solution_2(aoc_input: str):
    equations = parse_input(aoc_input)
    return sum(token_to_win(eq, offset=10_000_000_000_000) for eq in equations)

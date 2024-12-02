def parse_input(aoc_input: str) -> list[list[int]]:
    return [list(map(int, n.split())) for n in aoc_input.splitlines() if n != ""]


def is_safe(report: list[int], damp=False) -> bool:
    if report[-1] == report[0]:
        # catch edge case before it leeds to ZeroDivision error
        return False

    direction = (report[-1] - report[0]) / abs(report[-1] - report[0])

    for i in range(len(report) - 1):
        dist = (report[i + 1] - report[i]) * direction
        if dist < 1 or dist > 3:
            if damp and is_safe(report[0:i] + report[i + 1 :]):
                return True
            elif damp and is_safe(report[0 : i + 1] + report[i + 2 :]):
                return True
            else:
                return False
    return True


def solution_1(aoc_input: str) -> int:
    reports = parse_input(aoc_input)
    return len([r for r in reports if is_safe(r)])


def solution_2(aoc_input: str) -> int:
    reports = parse_input(aoc_input)
    return len([r for r in reports if is_safe(r, damp=True)])

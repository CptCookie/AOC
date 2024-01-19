from functools import cache


def parse_input(aoc_input: str) -> tuple[str, tuple[int]]:
    input = []
    for line in aoc_input.splitlines():
        springs, seq = line.split(" ")
        input.append((springs, tuple(int(n) for n in seq.split(","))))

    return input


@cache
def number_of_solutions(springs: str, seq: tuple[int, ...]) -> int:
    if seq == () and "#" not in springs:
        return 1
    if (
        seq
        and not springs
        or springs
        and not seq
        or sum(seq) + len(seq) - 1 > len(springs)
    ):
        return 0

    solutions = 0

    if springs[0] in [".", "?"]:
        # no sequence at the start
        solutions += number_of_solutions(springs[1:], seq)

    if springs[0] in ["#", "?"] and "." not in springs[: seq[0]]:
        # seq from the start on

        if len(springs) == seq[0]:
            solutions += number_of_solutions("", seq[1:])

        elif springs[seq[0]] != "#":
            solutions += number_of_solutions(springs[seq[0] + 1 :], seq[1:])

    return solutions


def number_of_expanded_solutions(springs: str, seq: tuple[int, ...]) -> int:
    springs = "?".join([springs] * 5)
    seq = seq * 5

    return number_of_solutions(springs, seq)


def solution_1(aoc_input: str) -> int:
    input = parse_input(aoc_input)
    return sum(number_of_solutions(springs, seq) for springs, seq in input)


def solution_2(aoc_input: str) -> int:
    input = parse_input(aoc_input)
    return sum(number_of_expanded_solutions(springs, seq) for springs, seq in input)

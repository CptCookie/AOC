from functools import cache


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


@cache
def max_bank_joltage(bank: str, digits=2) -> str:
    joltage = 0

    if len(bank) == 0:
        raise ValueError

    for n, a in enumerate(bank):
        try:
            if digits > 1:
                j = int(f"{a}{max_bank_joltage(bank[n + 1 :], digits - 1)}")
            else:
                j = int(a)
            if j > joltage:
                joltage = j
        except ValueError:
            pass
    return joltage


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return sum(int(max_bank_joltage(bank)) for bank in input)


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return sum(int(max_bank_joltage(bank, digits=12)) for bank in input)

from math import log10, floor


def parse_input(aoc_input: str):
    pairs = []

    for line in aoc_input.splitlines():
        result, elements = line.split(":")
        pairs.append((int(result), tuple(map(int, elements.split()))))
    return pairs


def is_combination_of(value: int, elements: tuple[int, ...], concat=False) -> bool:
    last = elements[-1]
    remain = elements[:-1]
    digits = floor(log10(last)) + 1

    if len(elements) == 1:
        return value == last

    if value % last == 0 and is_combination_of(value // last, remain, concat):
        return True

    if value - last > 0 and is_combination_of(value - last, remain, concat):
        return True

    if concat and value % 10**digits == last:
        new_value = value // 10**digits
        if is_combination_of(new_value, remain, concat):
            return True

    return False


def solution_1(aoc_input: str):
    pairs = parse_input(aoc_input)
    return sum(value for value, elements in pairs if is_combination_of(value, elements))


def solution_2(aoc_input: str):
    pairs = parse_input(aoc_input)
    return sum(
        value for value, elements in pairs if is_combination_of(value, elements, True)
    )

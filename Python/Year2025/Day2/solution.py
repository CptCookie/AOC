import re

PATTERN_SOLUTION_1 = re.compile(r"^(\d+)\1$")
PATTERN_SOLUTION_2 = re.compile(r"^(\d+)\1+$")


def parse_input(aoc_input: str) -> list[range]:
    product_ids = []
    pattern = r"(\d+)-(\d+)"
    for match in re.finditer(pattern, aoc_input):
        start, end = match.groups()
        product_ids.append(range(int(start), int(end) + 1))
    return product_ids


def get_matching_ids(product_ids: range, pattern: re.Pattern):
    return [pid for pid in product_ids if pattern.match(str(pid))]


def get_invalid_ids_complex(product_ids: range):
    invalid_ids = []
    pattern = re.compile(r"^(\d+)\1+$")

    for pid in product_ids:
        if pattern.match(str(pid)):
            invalid_ids.append(pid)

    return invalid_ids


def solution_1(aoc_input: str):
    ranges = parse_input(aoc_input)
    count = 0
    for id_range in ranges:
        count += sum(get_matching_ids(id_range, PATTERN_SOLUTION_2))
    return count


def solution_2(aoc_input: str):
    ranges = parse_input(aoc_input)
    count = 0
    for id_range in ranges:
        count += sum(get_matching_ids(id_range, PATTERN_SOLUTION_2))
    return count

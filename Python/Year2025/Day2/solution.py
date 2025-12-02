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


def get_matching_ids(product_ids: range, pattern: re.Pattern) -> list[int]:
    return [pid for pid in product_ids if pattern.match(str(pid))]


def calc_count_from_ranges(product_ids: list[range], match_pattern) -> int:
    count = 0
    for id_range in product_ids:
        count += sum(get_matching_ids(id_range, match_pattern))
    return count


def solution_1(aoc_input: str):
    ranges = parse_input(aoc_input)
    return calc_count_from_ranges(ranges, PATTERN_SOLUTION_1)


def solution_2(aoc_input: str):
    ranges = parse_input(aoc_input)
    return calc_count_from_ranges(ranges, PATTERN_SOLUTION_2)

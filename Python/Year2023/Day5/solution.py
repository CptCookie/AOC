import re
from typing import TypeAlias

Section: TypeAlias = list[tuple[int, int, int]]
Range: TypeAlias = tuple[int, int]


def parse_input(aoc_input: str) -> tuple[list[int], list[Section]]:
    seeds = []
    maps: list[Section] = []

    for i, s in enumerate(aoc_input.split("\n\n")):
        if i == 0:
            seeds = [int(n) for n in s.split(" ") if n.isalnum()]

        else:
            section: Section = []
            for m in re.finditer("(\d+) (\d+) (\d+)", s):
                match_group = m.groups()
                section.append(
                    (
                        int(match_group[0]),
                        int(match_group[1]),
                        int(match_group[2]),
                    )
                )
            maps.append(section)

    return seeds, maps


def map_value_by_section(value: int, maps: Section) -> int:
    for dstart, sstart, r in maps:
        if sstart <= value <= sstart + r:
            return dstart + value - sstart
    return value


def map_range_by_section(r: Range, maps: Section) -> list[Range]:
    mapped_ranges = []
    rstart, rend = r

    for dstart, sstart, l in maps:
        if sstart <= rstart <= sstart + l and sstart <= rend <= sstart + l:
            # [         (_____)    ]
            # completly included, return singe range
            mapped_ranges.append((dstart + rstart - sstart, dstart + rend - sstart))
            return mapped_ranges

        elif sstart <= rstart <= sstart + l and sstart + l < rend:
            # [    (____]   )
            # beginning included, shorten the range after calculation
            mapped_ranges.append((dstart + rstart - sstart, dstart + l))
            rstart = sstart + l

        elif rstart < sstart and sstart <= rend <= sstart + l:
            # (   [____)   )
            # end included, shorten the range after calculation
            mapped_ranges.append((dstart, dstart + rend - sstart))
            rend = sstart - 1

    mapped_ranges.append((rstart, rend))
    return mapped_ranges


def map_value_by_alma(value: int, almananch: list[Section]):
    for section in almananch:
        value = map_value_by_section(value, section)
    return value


def map_ranges_by_alma(ranges: list[Range], almananch: list[Section]):
    for section in almananch:
        n_range = []
        for r in ranges:
            n_range.extend(map_range_by_section(r, section))
        ranges = n_range

    return ranges


def solution_1(aoc_input: str) -> int:
    seeds, alma = parse_input(aoc_input)
    results = [map_value_by_alma(v, alma) for v in seeds]
    return min(results)


def solution_2(aoc_input: str) -> int:
    seeds, alma = parse_input(aoc_input)
    seed_ranges = [(start, start + l) for start, l in zip(*[iter(seeds)] * 2)]
    result_ranges = map_ranges_by_alma(seed_ranges, alma)
    return min(result_ranges, key=lambda x: x[0])[0]

import re


def parse_input(aoc_input: str) -> ([int], [[(int, int, int)]]):
    seeds = []
    maps = []

    for i, s in enumerate(aoc_input.split("\n\n")):
        if i == 0:
            seeds = [int(n) for n in s.split(" ") if n.isalnum()]

        else:
            section = []
            for m in re.finditer("(\d+) (\d+) (\d+)", s):
                section.append(tuple(int(n) for n in m.groups()))
            maps.append(section)

    return seeds, maps


def map_value_by_section(value: int, maps: [(int, int, int)]) -> int:
    for dstart, sstart, r in maps:
        if sstart <= value <= sstart + r:
            return dstart + value - sstart
    return value


def map_range_by_section(
    r: tuple[int, int], maps: [(int, int, int)]
) -> [tuple[int, int]]:
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


def map_value_by_alma(value: int, almananch: [[(int, int, int)]]):
    for section in almananch:
        value = map_value_by_section(value, section)
    return value


def map_ranges_by_alma(ranges: [tuple[int, int]], almananch: [[(int, int, int)]]):
    for section in almananch:
        n_range = []
        for r in ranges:
            n_range.extend(map_range_by_section(r, section))
        ranges = n_range

    return ranges


def solution_1(aoc_input: str):
    seeds, alma = parse_input(aoc_input)
    results = [map_value_by_alma(v, alma) for v in seeds]
    return min(results)


def solution_2(aoc_input: str):
    seeds, alma = parse_input(aoc_input)
    seed_ranges = [(start, start + l) for start, l in zip(*[iter(seeds)] * 2)]
    result_ranges = map_ranges_by_alma(seed_ranges, alma)
    return min(result_ranges, key=lambda x: x[0])[0]

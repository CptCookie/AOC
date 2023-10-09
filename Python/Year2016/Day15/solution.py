import re


def parse_input(aoc_input: str):
    pattern = r".*has (\d+).* position (\d+)"
    return [(int(m[0]), int(m[1])) for m in re.findall(pattern, aoc_input)]


def time_alignment(discs: list[tuple[int, int]]):
    time = 1
    total_periode = 1

    for pos, (size, start) in enumerate(discs[-1::-1]):
        for n in range(size):
            ctime = time + n * total_periode
            t_pos = (start + ctime) % size
            if t_pos == pos:
                total_periode = lcm(total_periode, size)
                time = ctime
                break  # move to next disk

    return time - len(discs)


def lcm(a, b):
    min_num = min([a, b])
    max_num = max([a, b])

    for i in range(1, a * b + 1):
        if (i * min_num) % max_num == 0:
            return i * min_num

    raise AttributeError(f"Could not find a LCM for {a} and {b}, [BUG]")


def solution_1(aoc_input: str):
    return time_alignment(parse_input(aoc_input))


def solution_2(aoc_input: str):
    discs = parse_input(aoc_input)
    discs.append((11, 0))
    return time_alignment(discs)

from typing import Optional, Iterable


def parse_input(aoc_input: str) -> list[list[str]]:
    lava_maps = []

    for m in aoc_input.split("\n\n"):
        lava_maps.append(m.splitlines())

    return lava_maps


def get_reflection(map: list[str], num_dif=0) -> Optional[int]:
    refl = []
    for n in range(1, len(map[0])):
        reflection_diffs = 0

        for line in map:
            left = reversed(line[:n])
            right = line[n:]
            reflection_diffs += sum(l != r for l, r in zip(left, right))

        if reflection_diffs == num_dif:
            refl.append(n)

    if len(refl) == 1:
        return refl.pop()
    elif len(refl) == 0:
        return None
    else:
        raise ValueError


def get_reflection_score(map: list[str], num_diff: int = 0) -> int:
    if hor := get_reflection(map, num_diff):
        return hor

    vert_map = ["".join([line[n] for line in map]) for n in range(len(map[0]))]
    if ver := get_reflection(vert_map, num_diff):
        return ver * 100

    raise ValueError("map has no reflection")


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return sum([get_reflection_score(m) for m in input])


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return sum([get_reflection_score(m, 1) for m in input])

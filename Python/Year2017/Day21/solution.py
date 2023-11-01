import re
from copy import deepcopy
from math import sqrt


def rotate_clock(pattern: tuple, n):
    if n > 1:
        pattern = rotate_clock(pattern, n - 1)

    rotated = []
    for x in range(len(pattern)):
        line = ""
        for y in range(len(pattern) - 1, -1, -1):
            line += pattern[y][x]
        rotated.append(line)
    return tuple(rotated)


def flip_hor(pattern: tuple) -> tuple:
    return tuple("".join(line[-1::-1]) for line in pattern)


def flip_vertical(pattern: tuple) -> tuple:
    return tuple(pattern[-1::-1])


def parse_input(puzzle_input: str) -> dict[tuple[str], tuple[str]]:
    pattern = r"([\.#]{2,3})\/([\.#]{2,3})\/?([\.#]{2,3})? => ([\.#]{3,4})\/([\.#]{3,4})\/([\.#]{3,4})\/?([\.#]{3,4})?"

    patterns = {}
    for m in re.finditer(pattern, puzzle_input):
        match m.groups():
            case r1, r2, None, p1, p2, p3, None:
                patterns[(r1, r2)] = (p1, p2, p3)
            case r1, r2, r3, p1, p2, p3, p4:
                patterns[(r1, r2, r3)] = (p1, p2, p3, p4)
            case _:
                raise ValueError(f"unexpected matches {m.groups()}")

    return patterns


def expand_patterns(
    patterns: dict[tuple[str], tuple[str]]
) -> dict[tuple[str], tuple[str]]:
    expanded = {}
    for p, r in patterns.items():
        expanded[p] = r
        for new_p in (
            rotate_clock(p, 1),
            rotate_clock(p, 2),
            rotate_clock(p, 3),
        ):
            if new_p in expanded and expanded[new_p] != r:
                raise ValueError("pattern already set")
            else:
                expanded[new_p] = r

    patterns = expanded

    expanded = {}
    for p, r in patterns.items():
        expanded[p] = r
        for new_p in (
            flip_hor(p),
            flip_vertical(p),
        ):
            if new_p in expanded and expanded[new_p] != r:
                raise ValueError("pattern already set")
            else:
                expanded[new_p] = r

    return expanded


def disassemble_display(display: list[str]):
    if len(display) % 2 == 0:
        mode = 2
    elif len(display) % 3 == 0:
        mode = 3
    else:
        raise ValueError(f"Can not disassemble {len(display)}")

    all_patches = []

    for sy in range(0, len(display), mode):
        for sx in range(0, len(display[0]), mode):
            all_patches.append(
                tuple(display[sy + dy][sx : sx + mode] for dy in range(mode))
            )
    return all_patches


def reassemble_display(patches):
    dimension = int(sqrt(len(patches)))
    display = []

    for x in range(0, len(patches), dimension):
        for y in range(len(patches[0])):
            display.append("".join(p[y] for p in patches[x : x + dimension]))

    return display


def solution_1(puzzle_input: str):
    patterns = parse_input(puzzle_input)
    patterns = expand_patterns(patterns)

    display = [".#.", "..#", "###"]

    for n in range(5):
        patches = disassemble_display(display)
        new_patches = [patterns[p] for p in patches]
        display = reassemble_display(new_patches)

    return sum([line.count("#") for line in display])


def solution_2(puzzle_input: str):
    patterns = parse_input(puzzle_input)
    patterns = expand_patterns(patterns)

    display = [".#.", "..#", "###"]

    for n in range(18):
        patches = disassemble_display(display)
        new_patches = [patterns[p] for p in patches]
        display = reassemble_display(new_patches)

    return sum([line.count("#") for line in display])

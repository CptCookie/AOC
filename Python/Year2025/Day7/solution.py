from functools import cache

SPLITTER = "^"


def parse_input(aoc_input: str) -> tuple[str, ...]:
    return tuple(n for n in aoc_input.splitlines() if n != "")


def split_tachion_beams(manyfold: tuple[str, ...]) -> int:
    beams_pos = set()
    beams_pos.add(next(x for x, n in enumerate(manyfold[0]) if n == "S"))
    split_counter = 0

    for line in manyfold[1:]:
        new_beam_pos = set()

        for x in beams_pos:
            if line[x] == SPLITTER:
                split_counter += 1
                new_beam_pos.add(x - 1)
                new_beam_pos.add(x + 1)
            else:
                new_beam_pos.add(x)

        beams_pos = new_beam_pos
    return split_counter


@cache
def split_time(manyfold: tuple[str, ...], beams_pos: tuple[int, int] = None) -> int:
    if not beams_pos:
        x = next(x for x, n in enumerate(manyfold[0]) if n == "S")
        y = 0
    else:
        x, y = beams_pos

    if y >= len(manyfold):
        return 1

    if manyfold[y][x] == SPLITTER:
        return split_time(manyfold, (x - 1, y + 1)) + split_time(
            manyfold, (x + 1, y + 1)
        )

    return split_time(manyfold, (x, y + 1))


def solution_1(aoc_input: str):
    manyfold = parse_input(aoc_input)
    return split_tachion_beams(manyfold)


def solution_2(aoc_input: str):
    manyfold = parse_input(aoc_input)
    return split_time(manyfold)

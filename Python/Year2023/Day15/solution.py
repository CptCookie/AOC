import re

PATTERN = r"([a-z]+)-|([a-z]+)=(\d)"


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.strip().split(",") if n != ""]


def hash_acsii(inp: str) -> int:
    value = 0
    for c in inp:
        value += ord(c)
        value *= 17
        value %= 256

    return value


def set_up_lenses(inp: str):
    boxes: list[dict[str, int]] = [dict() for _ in range(256)]
    for m in re.finditer(PATTERN, inp):
        match m.groups():
            case (None, label, number):
                # add or replace lens
                boxes[hash_acsii(label)][label] = int(number)
            case (label, None, None):
                # remove lens
                idx = hash_acsii(label)
                if label in boxes[idx]:
                    boxes[idx].pop(label)
    return boxes


def calc_focus_power(boxes: list[dict[str, int]]) -> int:
    total_focus = 0
    for box_num, box in enumerate(boxes):
        for lens_pos, k in enumerate(box.keys()):
            total_focus += (box_num + 1) * (lens_pos + 1) * box[k]

    return total_focus


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    return sum(hash_acsii(s) for s in input)


def solution_2(aoc_input: str):
    boxes = set_up_lenses(aoc_input)
    return calc_focus_power(boxes)

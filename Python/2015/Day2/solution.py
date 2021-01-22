import math
from typing import List


def parse_input(puzzle_input):
    box_dimension = []
    for box in puzzle_input.split("\n"):
        if box != "":
            box_dimension.append([int(n) for n in box.split("x")])
    return box_dimension


def total_wrapping_paper(puzzle_input: str):
    boxes = parse_input(puzzle_input)
    paper = [paper_needed(n) for n in boxes]
    return sum(paper)


def paper_needed(box: List[int]) -> int:
    areas = [box[0] * box[1], box[1] * box[2], box[0] * box[2]]
    return min(areas) + sum(areas) * 2


def total_material_needed(puzzle_input, material_func):
    boxes = parse_input(puzzle_input)
    paper = [material_func(n) for n in boxes]
    return sum(paper)


def ribbon_needed(box: List[int]):
    return sum(sorted(box)[:-1]) * 2 + math.prod(box)


def solution_1(puzzle_input):
    return total_material_needed(puzzle_input, paper_needed)


def solution_2(puzzle_input):
    return total_material_needed(puzzle_input, ribbon_needed)

import math
from typing import List, Callable
from collections import namedtuple


class Box:
    def __init__(self, x, y, z):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def wrapping_needed(self) -> int:
        areas = [self.x * self.y, self.y * self.z, self.x * self.z]
        return min(areas) + sum(areas) * 2

    def ribbon_needed(self) -> int:
        ribbon_sides = sorted([self.x, self.y, self.z])[:-1]
        bow = self.x * self.y * self.z
        return sum(ribbon_sides) * 2 + bow


def parse_puzzel_string(puzzle_string: str) -> List[Box]:
    box_dimensions = []
    for box in puzzle_string.split("\n"):
        if box != "":
            box = Box(*box.split("x"))
            box_dimensions.append(box)
    return box_dimensions


def total_material_needed(all_boxes: List[Box], material_function: Callable) -> int:
    material = [material_function(box) for box in all_boxes]
    return sum(material)


def solution_1(puzzle_string: str) -> int:
    all_boxes = parse_puzzel_string(puzzle_string)
    return total_material_needed(all_boxes, Box.wrapping_needed)


def solution_2(puzzle_string: str) -> int:
    all_boxes = parse_puzzel_string(puzzle_string)
    return total_material_needed(all_boxes, Box.ribbon_needed)

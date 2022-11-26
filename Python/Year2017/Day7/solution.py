import re
from statistics import mean
from typing import Optional

regex = r"(\w+) \((\d+)\).{0,4}([\w, ]+)?"

def parse_data(puzzle_input: str) -> list[tuple[str, int, Optional[list[str]]]]:
    puzzle_data = []

    for line in puzzle_input.splitlines():
        groups = re.match(regex, line).groups()

        root = groups[0]
        value = int(groups[1])
        childs = []
        if len(groups) > 2 and groups[2] is not None:
            childs = groups[2].replace(" ", "").split(",")
        puzzle_data.append([root, value, childs])

    return puzzle_data

def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    return get_root( data ).pop()


def get_root( data ):
    childs = [ n[ 2 ] for n in data if len( n ) > 2 ]
    childs = {elem for line in childs for elem in line}
    roots = {n[ 0 ] for n in data}
    return roots.difference( childs )


def solution_2(puzzle_input: str) -> int:
    data = parse_data(puzzle_input)
    nodes = dict()
    solutions = []
    for line in data:
        nodes[line[0]] = line

    def get_wight(name: str):
        if len(nodes[name]) > 2:
            return nodes[name][1] + sum(get_wight(c) for c in nodes[name][2])


    for name, current_node in nodes.items():
        if len(current_node) > 2:
            child_values = {c:get_wight(c) for c in current_node[2]}
            if any(v != mean(child_values.values()) for v in child_values.values()):
                bad_child = [name for name, value in child_values.items() if list(child_values.values()).count(value) == 1][0]
                good_child = [name for name, value in child_values.items() if list(child_values.values()).count(value) > 1][0]

                solutions.append(nodes[bad_child][1] + child_values[good_child] - child_values[bad_child])

    return min(solutions)


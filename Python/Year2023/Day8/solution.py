import re
from itertools import cycle
from math import gcd
from typing import TypeAlias

Node: TypeAlias = tuple[str, str]
NodeMap: TypeAlias = dict[str, Node]

LEFT = "L"
RIGHT = "R"


def parse_input(aoc_input: str) -> tuple[str, NodeMap]:
    instr, node = aoc_input.split("\n\n")

    node_dict: NodeMap = {}
    for m in re.finditer("([\dA-Z]{3}) = \(([\dA-Z]{3}), ([\dA-Z]{3})\)", node):
        name, left, right = m.groups()
        node_dict[name] = (left, right)

    return instr.strip(), node_dict


def single_route_len(instr: str, nodes: NodeMap):
    current_node = "AAA"
    l = 0

    for i in cycle(instr):
        if current_node == "ZZZ":
            return l

        l += 1
        if i == LEFT:
            current_node = nodes[current_node][0]
        else:
            current_node = nodes[current_node][1]


def lcm(seq: list[int]) -> int:
    value = 1
    for n in seq:
        value = value * n // gcd(value, n)
    return value


def multi_route_len(instructions: str, nodes: NodeMap):
    path_nodes = [n for n in nodes.keys() if n.endswith("A")]
    last: list[int | None] = [None for _ in path_nodes]
    loops: list[int | None] = [None for _ in path_nodes]

    for n, instr in enumerate(cycle(instructions)):
        path_nodes = [nodes[n][0] if instr == LEFT else nodes[n][1] for n in path_nodes]

        for idx, cnode in enumerate(path_nodes):
            if cnode.endswith("Z") and loops[idx] is None and last[idx] is None:
                # seen end of route the first time
                last[idx] = n

            elif cnode.endswith("Z") and loops[idx] is None and last[idx] is not None:
                # seen end of route the second time -> loop detected
                loops[idx] = n - last[idx]

            if all(l is not None for l in loops):
                # all loops found
                return lcm(loops)


def solution_1(aoc_input: str):
    instr, nodes = parse_input(aoc_input)
    return single_route_len(instr, nodes)


def solution_2(aoc_input: str):
    instr, nodes = parse_input(aoc_input)
    return multi_route_len(instr, nodes)

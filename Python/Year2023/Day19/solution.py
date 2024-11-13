import re
from operator import add
from functools import reduce
from typing import TypeAlias

Rules: TypeAlias = list[str]
Workflows = dict[str, Rules]
Part: TypeAlias = dict[str, int]
PartRange: TypeAlias = dict[str, range]


def parse_workflow(aoc_input: str) -> dict[str, list[str]]:
    parsed_workflow = {}
    workflow, _ = aoc_input.split("\n\n")
    for line in workflow.splitlines():
        key, flow = line.split("{")
        parsed_workflow[key] = flow.replace("}", "").split(",")
    return parsed_workflow


def parse_parts(aoc_input: str) -> list[Part]:
    parts = []
    for match in re.finditer(r"{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}", aoc_input):
        x, m, a, s = match.groups()
        parts.append({"x": int(x), "m": int(m), "a": int(a), "s": int(s)})
    return parts


def get_flow_outcome(part: Part, rules: Rules):
    for r in rules:
        if ":" not in r:
            # default case
            return r
        c, o = r.split(":")
        attr, comp, number = c[0], c[1], int(c[2:])
        if comp == ">" and part[attr] > number:
            return o
        if comp == "<" and part[attr] < number:
            return o


def get_ranged_flow_outcome(part: PartRange, rules: Rules):
    outcomes: list[tuple[str, PartRange]] = []
    for r in rules:
        if ":" not in r:
            # default case
            outcomes.append((r, part))
            return outcomes

        c, o = r.split(":")
        attr, comp, number = c[0], c[1], int(c[2:])

        if part[attr].start <= number <= part[attr].stop:
            if comp == "<":
                outcomes.append((o, {**part, attr: range(part[attr].start, number)}))
                part[attr] = range(number, part[attr].stop)
            if comp == ">":
                outcomes.append((o, {**part, attr: range(number + 1, part[attr].stop)}))
                part[attr] = range(part[attr].start, number + 1)


def get_valid_parts(parts: list[Part], workflows: Workflows) -> list[Part]:
    valid = []

    for p in parts:
        flow = "in"
        while True:
            flow = get_flow_outcome(p, workflows[flow])
            if flow == "A":
                valid.append(p)
            if flow == "A" or flow == "R":
                break
    return valid


def get_valid_part_ranges(workflows: Workflows) -> list[PartRange]:
    valid: list[PartRange] = []
    stack: list[tuple[str, PartRange]] = [
        (
            "in",
            {key: range(1, 4001) for key in "xmas"},
        )
    ]

    while stack:
        flow_name, part = stack.pop()
        outs = get_ranged_flow_outcome(part, workflows[flow_name])

        for flow_name, part in outs:
            if flow_name == "A":
                valid.append(part)
            elif flow_name != "R":
                stack.append((flow_name, part))

    return valid


def calculate_value(part: Part) -> int:
    return reduce(add, part.values())


def calculate_ranged_value(part: PartRange) -> int:
    value = 1
    for r in part.values():
        value *= r.stop - r.start
    return value


def solution_1(aoc_input: str):
    workflows = parse_workflow(aoc_input)
    parts = parse_parts(aoc_input)

    valid = get_valid_parts(parts, workflows)
    return sum(calculate_value(p) for p in valid)


def solution_2(aoc_input: str):
    workflow = parse_workflow(aoc_input)
    valid = get_valid_part_ranges(workflow)
    return sum(calculate_ranged_value(v) for v in valid)

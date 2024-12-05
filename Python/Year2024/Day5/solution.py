import re
from collections import defaultdict


def parse_rules(aoc_input: str) -> dict[int, set[int]]:
    ordering_rules = defaultdict(set)

    for match in re.finditer(r"(\d+)\|(\d+)", aoc_input):
        pre, post = match.groups()
        ordering_rules[int(pre)].add(int(post))

    return ordering_rules


def parse_updates(aoc_input: str) -> list[list[int]]:
    _, updates = aoc_input.split("\n\n")
    manual_updates = []

    for line in updates.splitlines():
        if line.strip() != "":
            manual_updates.append(list(map(int, line.split(","))))

    return manual_updates


def in_correct_order(update: list[int], ordering_rules: dict[int, list[int]]):
    for i, current in enumerate(update[:-1]):
        if current not in ordering_rules:
            return False
        if not all(post in ordering_rules[current] for post in update[i + 1 :]):
            return False
    return True


def fix_ordering(update: list[int], ordering_rules: dict[int, list[int]]) -> list[int]:
    new_ordering = []

    for n in update:
        if not new_ordering:
            new_ordering.append(n)
        elif in_correct_order([n] + new_ordering, ordering_rules):
            new_ordering = [n] + new_ordering
        else:
            new_ordering = insert_at_correct_position(new_ordering, n, ordering_rules)

    return new_ordering


def insert_at_correct_position(
    sequence: list[int], new_item: int, ordering_rules: dict[int, list[int]]
):
    for new_idx in range(len(sequence)):
        new_seq = sequence[:new_idx] + [new_item] + sequence[new_idx:]
        if in_correct_order(new_seq, ordering_rules):
            return new_seq
    return sequence + [new_item]


def solution_1(aoc_input: str):
    rules = parse_rules(aoc_input)
    updates = parse_updates(aoc_input)
    count = 0
    for update in updates:
        if in_correct_order(update, rules):
            count += update[len(update) // 2]
    return count


def solution_2(aoc_input: str):
    rules = parse_rules(aoc_input)
    updates = parse_updates(aoc_input)
    count = 0
    for update in updates:
        if not in_correct_order(update, rules):
            fixed_order = fix_ordering(update, rules)
            count += fixed_order[len(fixed_order) // 2]
    return count

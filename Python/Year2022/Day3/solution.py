from functools import reduce


def parse_data(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.splitlines() if n != ""]


def find_wrong_item(rucksack: str):
    compartment_1 = set(rucksack[len(rucksack) // 2 :])
    compartment_2 = set(rucksack[: len(rucksack) // 2])

    return compartment_1.intersection(compartment_2).pop()


def get_priority(item: str):
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def find_auth_badge(rucksacks: list[str]) -> str:
    if len(rucksacks) != 3:
        raise ValueError("Only 3 Rucksacks belong together")

    common_items = reduce(lambda x, y: x.intersection(y), [set(r) for r in rucksacks])
    return common_items.pop()


def solution_1(puzzle_input: str):
    rucksacks = parse_data(puzzle_input)
    wrong_items = [find_wrong_item(r) for r in rucksacks]
    return sum([get_priority(i) for i in wrong_items])


def solution_2(puzzle_input: str):
    rucksacks = parse_data(puzzle_input)
    total_prio = 0
    for i in range(len(rucksacks) // 3):
        groupe = rucksacks[i * 3 : (i + 1) * 3]
        total_prio += get_priority(find_auth_badge(groupe))
    return total_prio

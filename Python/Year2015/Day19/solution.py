import re
from copy import deepcopy

elem_regex = re.compile(r"e|[A-Z]{1}[a-z]?")


def parse_substitutions(lst):
    subs = []
    for line in lst:
        raw = line.replace(" => ", " ").split(" ")
        subs.append((raw[0], raw[1]))
    return subs


def get_all_products(molekule, subs):
    start_mol_elem = elem_regex.findall(molekule)
    print(len(start_mol_elem))
    all_product = []

    for s in subs:
        for n, element in enumerate(start_mol_elem):
            if element == s[0]:
                mol_copy = deepcopy(start_mol_elem)
                before = mol_copy[:n]
                after = mol_copy[n + 1 :] if n < len(mol_copy) - 1 else []
                all_product.append("".join(before + [s[1]] + after))
    return all_product


def count_Element(element, molekule):
    return elem_regex.findall(molekule).count(element)


def get_number_of_steps_to(molekule):
    # specific solution based on
    # https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
    return (
        len(elem_regex.findall(molekule))
        - 2 * count_Element("Ar", molekule)
        - 2 * count_Element("Y", molekule)
        - 1
    )


def get_unique(lst):
    return [elem for n, elem in enumerate(lst) if lst.index(elem) == n]


def regex_replace(match, string: str, replace: str) -> str:
    return f"{string[: match.start()]}{replace}{string[match.end() :]}"


def solution_1(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    substitutions = parse_substitutions(puzzle_input[:-1])
    products = get_all_products(puzzle_input[-1], substitutions)
    return len(get_unique(products))


def solution_2(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    return get_number_of_steps_to(puzzle_input[-1])

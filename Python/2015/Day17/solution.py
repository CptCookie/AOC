from itertools import chain, combinations, filterfalse


def get_all_valid_combination(container, sum_amount):
    valid = []
    for c in chain.from_iterable(
        combinations(container, r) for r in range(len(container) + 1)
    ):
        if sum(c) == sum_amount:
            valid.append(list(c))
    return valid


def solve(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.split("\n") if n != ""]
    valid_container = get_all_valid_combination(puzzle_input, 150)
    print(f"solution 1: {len(valid_container)}")

    min_number_container = min([len(n) for n in valid_container])
    print(
        f"solution 2: {len([n for n in valid_container if len(n) == min_number_container])}"
    )

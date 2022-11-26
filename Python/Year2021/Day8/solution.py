def get_value(sequence: list[set[str]], output_number: list[set[str]]):
    # fmt: off
    numbers = [None] * 10
    numbers[1] = sequence[0]
    numbers[7] = sequence[1]
    numbers[4] = sequence[2]
    numbers[8] = sequence[9]
    numbers[9] = [n for n in sequence if len(n) == 6 and n.issuperset(numbers[4])][0]
    numbers[0] = [n for n in sequence if len(n) == 6 and n.issuperset(numbers[1]) and n != numbers[9]][0]
    numbers[6] = [n for n in sequence if len(n) == 6 and n != numbers[0] and n != numbers[9]][0]
    numbers[3] = [n for n in sequence if len(n) == 5 and n.issuperset(numbers[7])][0]
    numbers[5] = [n for n in sequence if len(n) == 5 and n.issubset(numbers[6])][0]
    numbers[2] = [n for n in sequence if len(n) == 5 and n != numbers[3] and n != numbers[5]][0]
    # fmt: on
    return sum(
        numbers.index(s) * pow(10, i) for i, s in enumerate(reversed(output_number))
    )


def solution_1(puzzle_input: str):
    puzzle_data = [n.split("|") for n in puzzle_input.splitlines()]
    output_values = [m for n in puzzle_data for m in n[1].split(" ")]

    return len([n for n in output_values if len(n) in [2, 3, 4, 7]])


def solution_2(puzzle_input: str):
    puzzle_data = [n.split("|") for n in puzzle_input.splitlines() if n != ""]
    value = 0
    for line in puzzle_data:
        sequence = sorted(
            [set(n) for n in line[0].split(" ") if n not in ["", " "]],
            key=lambda x: len(x),
        )
        output_number = [set(n) for n in line[1].split(" ") if n not in ["", " "]]
        value += get_value(sequence, output_number)

    return value

def get_unique_answers(passengers: list[str]) -> set[str]:
    answers = [n for m in passengers for n in list(m)]
    return set(answers)


def get_unanimous_answers(passengers: list[str]) -> set[str]:
    unique_answers = get_unique_answers(passengers)
    unanimous = set()
    for answer in unique_answers:
        if all([answer in n for n in passengers]):
            unanimous.add(answer)
    return unanimous


def solution_1(puzzle_input):
    passengers = [n.split("\n") for n in puzzle_input.split("\n\n") if n != ""]
    return sum([len(get_unique_answers(n)) for n in passengers])


def solution_2(puzzle_input):
    passengers = [n.split("\n") for n in puzzle_input.split("\n\n") if n != ""]
    return sum([len(get_unanimous_answers(n)) for n in passengers])

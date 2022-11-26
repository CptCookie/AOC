def get_unique_answers(passengers: [str]) -> int:
    answers = [n for m in passengers for n in list(m)]
    return set(answers)


def get_unanimous_answers(passengers: [str]) -> int:
    unique_answers = get_unique_answers(passengers)
    unanimous = set()
    for answer in unique_answers:
        if all([answer in n for n in passengers]):
            unanimous.add(answer)
    return unanimous


def solve(puzzle_input):
    passengers = [n.split("\n") for n in puzzle_input.split("\n\n") if n != ""]
    print(f"solution 1:{sum([len(get_unique_answers(n)) for n in passengers])}")
    print(f"solution 2:{sum([len(get_unanimous_answers(n)) for n in passengers])}")

MATCH_SCORES_1 = {
    ("A", "X"): 3,
    ("A", "Y"): 6,
    ("A", "Z"): 0,
    ("B", "X"): 0,
    ("B", "Y"): 3,
    ("B", "Z"): 6,
    ("C", "X"): 6,
    ("C", "Y"): 0,
    ("C", "Z"): 3,
}

SELECT_SCORE_1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

SELECT_SCORE_2 = {
    ("A", "X"): 3,
    ("A", "Y"): 1,
    ("A", "Z"): 2,
    ("B", "X"): 1,
    ("B", "Y"): 2,
    ("B", "Z"): 3,
    ("C", "X"): 2,
    ("C", "Y"): 3,
    ("C", "Z"): 1,
}

MATCH_SCORES_2 = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}


def parse_data(puzzle_input: str) -> list[list[str]]:
    return [n.split(" ") for n in puzzle_input.splitlines() if n != ""]


def solution_1(puzzle_input: str):
    data = parse_data(puzzle_input)
    return sum(
        [SELECT_SCORE_1[santa] + MATCH_SCORES_1[(elf, santa)] for elf, santa in data]
    )


def solution_2(puzzle_input: str):
    data = parse_data(puzzle_input)
    return sum(
        [MATCH_SCORES_2[result] + SELECT_SCORE_2[(elf, result)] for elf, result in data]
    )

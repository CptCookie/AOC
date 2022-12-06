def find_destinct_chars(msg: str, length: int) -> int:
    for i in range(length, len(msg)):
        window = msg[i - length : i]
        if len(set(window)) == len(window):
            return i


def solution_1(puzzle_input: str):
    return find_destinct_chars(puzzle_input[:-1], 4)


def solution_2(puzzle_input: str):
    return find_destinct_chars(puzzle_input[:-1], 14)

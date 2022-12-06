def find_destinct_chars(msg: str, length: int) -> int:
    for i in range(length, len(msg) - length):
        if len(set(msg[i - length : i])) == len(msg[i - length : i]):
            return i
    return None


def solution_1(puzzle_input: str):
    return find_destinct_chars(puzzle_input[:-1], 4)


def solution_2(puzzle_input: str):
    return find_destinct_chars(puzzle_input[:-1], 14)

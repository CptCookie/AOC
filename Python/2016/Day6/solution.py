from typing import List


def read_chars(lines: List[str]) -> List[str]:
    chars = [""] * len(lines[0])
    for l in lines:
        for i, c in enumerate(l):
            chars[i] += c
    return chars


def correct_message(lines: List[str], index=0) -> str:
    pos_chars = read_chars(lines)
    message = ""

    for chars in pos_chars:
        sorted_chars = sorted(
            list(set(chars)), key=lambda x: chars.count(x), reverse=True
        )
        message += sorted_chars[index]
    return message


def solution_1(puzzle_input: str):
    return correct_message([n for n in puzzle_input.splitlines() if n != ""])


def solution_2(puzzle_input):
    return correct_message([n for n in puzzle_input.splitlines() if n != ""], index=-1)

from typing import Tuple

letters = "zyxwvutsrqponmlkjihgfedcba"


def valid_room_name(name, checksum) -> bool:
    room_name = [c for c in name if c.isalpha()]
    most_common_lettes = sorted(
        list(set(room_name)), key=lambda x: sort_id(x, room_name), reverse=True
    )

    return all(c in checksum for c in most_common_lettes[:5])


def sort_id(char, search_str):
    return search_str.count(char) * 26 + letters.index(char)


def parse_line(line: str) -> Tuple[str]:
    import re

    regex = re.search(r"([a-z\-]+)([\d\-]+)\[([a-z]{5})\]", line)
    if regex is not None:
        return regex.groups()
    else:
        return None, None, None


def decrypt_name(name: str, n_rotate: int) -> str:
    return "".join([rotate_char(c, n_rotate) for c in name.replace("-", " ")])


def rotate_char(char, n_rotate):
    if char.isalpha():
        return letters[letters.index(char) - n_rotate % 26]
    else:
        return char


def solution_1(puzzle_input: str):
    id_sum = 0
    for line in puzzle_input.splitlines():
        r_name, r_id, r_checksum = parse_line(line)
        if r_name and valid_room_name(r_name, r_checksum):
            id_sum += int(r_id)
    return id_sum


def solution_2(puzzle_input: str):
    for line in puzzle_input.splitlines():
        r_name, r_id, r_checksum = parse_line(line)
        if r_name and valid_room_name(r_name, r_checksum):
            real_name = decrypt_name(r_name, int(r_id))
            if "northpole" in real_name:
                return r_id

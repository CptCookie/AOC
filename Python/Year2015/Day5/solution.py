alphabet = "abcdefghijklmnopqrstuvwxyz"
vowls = "aeiuo"
doubles = [n + n for n in alphabet]
disalow = ["ab", "cd", "pq", "xy"]


def is_valid_string_v1(text: str):
    if sum([text.count(n) for n in vowls]) < 3:
        return False
    if not any([n in text for n in doubles]):
        return False
    if any([n in text for n in disalow]):
        return False
    return True


def is_valid_string_v2(text):
    return has_double(text) and has_two_apart(text)


def has_double(text):
    pairs = [text[n] + elem for n, elem in enumerate(text[1:])]
    return any([text.index(n) + 1 < text.rindex(n) for n in pairs])


def has_two_apart(text):
    return any([text[n] == elem for n, elem in enumerate(text[2:])])


def solution_1(puzzle_input):
    all_texts = [n for n in puzzle_input.split("\n") if n != ""]
    return len([text for text in all_texts if is_valid_string_v1(text)])


def solution_2(puzzle_input):
    all_texts = [n for n in puzzle_input.split("\n") if n != ""]
    return len([text for text in all_texts if not is_valid_string_v2(text)])

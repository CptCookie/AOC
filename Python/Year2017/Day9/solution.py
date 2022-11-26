def parse_data(puzzle_input: str) -> str:
    return puzzle_input.replace("\n", "").replace("", "")


def remove_invert(text: str) -> str:
    while "!" in text:
        idx = text.find("!")
        text = text[:idx] + text[idx + 2 :]
    return text


def remove_garbage(text: str) -> tuple[str, int]:
    total_del = 0
    if "!" in text:
        text = remove_invert(text)

    while ">" in text:
        opening = None
        for i, c in enumerate(text):
            if c == "<" and opening is None:
                opening = i
            if c == ">" and opening is not None:
                total_del += i - opening - 1
                text = text[:opening] + text[i + 1 :]
                break
    return text, total_del


def count_value(text):
    if "!" in text:
        text = remove_invert(text)

    if "<" in text:
        text, _ = remove_garbage(text)

    depth = 0
    total_value = 0
    for c in text:
        if c == "{":
            depth += 1

        if c == "}":
            total_value += depth
            depth -= 1
    return total_value


def solution_1(puzzle_input: str):
    stream = parse_data(puzzle_input)
    return count_value(puzzle_input)


def solution_2(puzzle_input: str):
    stream = parse_data(puzzle_input)
    text, amount_gar = remove_garbage(puzzle_input)
    return amount_gar

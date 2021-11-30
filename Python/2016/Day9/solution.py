import re


def decompressed_length(string: str, recursive=False):
    numbers = []
    index = 0
    while string:
        match = re.search(r"\((\d+)x(\d+)\)", string[index:])
        if match:
            start, end = match.span()
            letters, repetition = [int(i) for i in match.groups()]
            numbers.append(len(string[:start]))

            seq = string[end : end + letters]

            if "(" in seq and recursive:
                numbers.append(decompressed_length(seq, recursive) * repetition)
            else:
                numbers.append(len(seq) * repetition)

            string = string[end + letters :]
        else:
            numbers.append(len(string))
            string = ""
    return sum(numbers)


def solution_1(puzzle_input: str):
    file = "".join([c for c in puzzle_input if c not in [" ", "\n"]])
    return decompressed_length(file)


def solution_2(puzzle_input: str):
    file = "".join([c for c in puzzle_input if c not in [" ", "\n"]])
    return decompressed_length(file, recursive=True)

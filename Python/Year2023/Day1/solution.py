number_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def find_number(line: str) -> int:
    first = ""
    for i, c in enumerate(line):
        if c.isdigit():
            first = c
        for num in number_words:
            if line[: i + 1].endswith(num):
                first = number_words[num]
                break
        if first != "":
            break

    last = ""
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            last = line[i]
        for num in number_words:
            if line[i:].startswith(num):
                last = number_words[num]
        if last != "":
            break

    return int(first + last)


def get_number(line):
    numbers = [n for n in line if n.isdigit()]
    if len(numbers) == 1:
        return int(numbers[0] + numbers[0])
    else:
        return int(numbers[0] + numbers[-1])


def solution_1(aoc_input: str):
    lines = parse_input(aoc_input)
    return sum(get_number(l) for l in lines)


def solution_2(aoc_input: str):
    lines = parse_input(aoc_input)
    return sum(find_number(l) for l in lines)

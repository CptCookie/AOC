def parse_data(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.splitlines() if n != ""]


def no_duplication(phrase: str) -> bool:
    return len(set(phrase.split(" "))) == phrase.count(" ") + 1


def no_anagrams(phrase: str) -> bool:
    words = set("".join(sorted(w)) for w in phrase.split(" "))
    return len(words) == len(phrase.split(" "))


def solution_1(puzzle_input: str):
    phrases = parse_data(puzzle_input)
    return len(list(filter(no_duplication, phrases)))


def solution_2(puzzle_input: str):
    phrases = parse_data(puzzle_input)
    return len(list(filter(no_anagrams, phrases)))

from typing import List


def get_babs(sections: List[str]) -> List[str]:
    babs = []
    for s in sections:
        for i in range(len(s) - 2):
            if s[i] == s[i + 2] != s[i + 1]:
                babs.append(s[i : i + 3])
    return babs


def supports_ssl(sections: List[str]) -> bool:
    babs = get_babs([s for s in sections[::2]])
    abas = [bab[1] + bab[:2] for bab in babs]
    return any([aba in s for s in sections[1::2] for aba in abas])


def contains_abba(string: str) -> bool:
    for i in range(len(string) - 3):
        if (
            string[i : i + 2] == string[i + 3 : i + 1 : -1]
            and string[i] != string[i + 1]
        ):
            return True
    return False


def supports_abba(sections: List[str]) -> bool:
    return any([contains_abba(s) for s in sections[::2]]) and not any(
        [contains_abba(s) for s in sections[1::2]]
    )


def parse_address_to_list(address: str) -> List[str]:
    return [n for n in address.replace("]", "[").split("[")]


def solution_1(puzzle_input: str) -> int:
    puzzle_input = [n for n in puzzle_input.splitlines()]
    return len([n for n in puzzle_input if supports_abba(parse_address_to_list(n))])


def solution_2(puzzle_input: str):
    puzzle_input = [n for n in puzzle_input.splitlines()]
    return len([n for n in puzzle_input if supports_ssl(parse_address_to_list(n))])

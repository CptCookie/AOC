def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def contains_multiples(s: str, n: int):
    chars = set(s)
    return any(s.count(c) == n for c in chars)


def common_id(boxes):
    for n, left in enumerate(boxes):
        for right in boxes[n + 1 :]:
            difs = [n for n in zip(left, right) if n[0] != n[1]]
            if len(difs) == 1:
                return "".join(n[0] for n in zip(left, right) if n[0] == n[1])


def solution_1(aoc_input: str):
    boxes = parse_input(aoc_input)
    return len([n for n in boxes if contains_multiples(n, 2)]) * len(
        [n for n in boxes if contains_multiples(n, 3)]
    )


def solution_2(aoc_input: str):
    boxes = parse_input(aoc_input)
    return common_id(boxes)

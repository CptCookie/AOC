from typing import Sequence


def parse_input(aoc_input: str) -> Sequence[tuple[set[int], set[int]]]:
    cards = []
    for line in aoc_input.strip().splitlines():
        _, card = line.split(": ")
        draw, win = card.split(" | ")
        draw_nums = set(int(n) for n in draw.split(" ") if n != "")
        win_nums = set(int(n) for n in win.split(" ") if n != "")
        cards.append((draw_nums, win_nums))
    return cards


def solution_1(aoc_input: str) -> int:
    cards = parse_input(aoc_input)
    score = 0

    for draw, win in cards:
        matches = len(draw.intersection(win))
        if matches > 0:
            score += 2 ** (matches - 1)
    return score


def solution_2(aoc_input: str) -> int:
    cards = parse_input(aoc_input)
    card_nums = [1 for _ in cards]

    for i, (draw, win) in enumerate(cards):
        for m in range(len(draw.intersection(win))):
            card_nums[i + m + 1] += card_nums[i]

    return sum(card_nums)

import re
from collections import deque


def parse_input(aoc_input: str) -> (int, int):
    pattern = r"(\d+) players; last marble is worth (\d+) points"
    return tuple(int(n) for n in re.match(pattern, aoc_input).groups())


def play_marbel(n_players, last_marbel):
    circle = deque([0])
    players = [0] * n_players

    for marbel in range(1, last_marbel + 1):
        if marbel % 23 == 0:
            circle.rotate(7)
            players[marbel % n_players] += circle.pop() + marbel
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marbel)

    return players, circle


def solution_1(aoc_input: str):
    n_player, last_value = parse_input(aoc_input)
    scores, circle = play_marbel(n_player, last_value)
    return max(scores)


def solution_2(aoc_input: str):
    n_player, last_value = parse_input(aoc_input)
    scores, circle = play_marbel(n_player, last_value * 100)
    return max(scores)

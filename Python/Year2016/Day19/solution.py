from collections import deque


def play_white_elephant_easy(seats: int):
    players = [n for n in range(seats)]

    while len(players) > 1:
        odd = len(players) % 2 == 1
        players = [p for i, p in enumerate(players) if i % 2 == 0]

        if odd:
            players = players[1:]

    return players.pop() + 1


def play_white_elephant_complex(seats: int):
    players = [n for n in range(1, seats + 1)]

    while len(players) > 1:
        odd = len(players) % 2 == 1
        lower_halve = players[len(players) // 2 :]
        filtered_halve = [
            n
            for i, n in enumerate(lower_halve)
            if not odd and i % 3 == 2 or odd and i % 3 == 1
        ]
        removed = len(lower_halve) - len(filtered_halve)

        players = (
            players[removed : len(players) // 2] + filtered_halve + players[:removed]
        )

    return players.pop()


def solution_1(aoc_input: str):
    nelfs = int(aoc_input.strip())
    return play_white_elephant_easy(nelfs)


def solution_2(aoc_input: str):
    nelfs = int(aoc_input.strip())
    return play_white_elephant_complex(nelfs)

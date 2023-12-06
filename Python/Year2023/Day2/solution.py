GREEN = "green"
BLUE = "blue"
RED = "red"

MAX_COLOR = {GREEN: 13, BLUE: 14, RED: 12}


def parse_input(aoc_input: str):
    games = []
    for line in aoc_input.splitlines():
        ids, draws = line.split(":")
        game_pairs = []

        for pair in draws.split(";"):
            pairs = []

            for color in pair.split(","):
                _, i, c = color.split(" ")
                pairs.append((int(i), c))
            game_pairs.append(pairs)
        games.append(game_pairs)
    return games


def game_possible(game):
    for pair in game:
        for i, c in pair:
            if MAX_COLOR[c] < i:
                return False
    return True


def pow_min_cubes(game):
    value = 1
    for color in MAX_COLOR:
        value *= max(n for pair in game for n, c in pair if c == color)
    return value


def solution_1(aoc_input: str):
    games = parse_input(aoc_input)
    games_possible = [i + 1 for i, g in enumerate(games) if game_possible(g)]
    return sum(games_possible)


def solution_2(aoc_input: str):
    games = parse_input(aoc_input)
    return sum(pow_min_cubes(game) for game in games)

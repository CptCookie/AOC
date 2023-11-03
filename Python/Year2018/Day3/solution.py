import re

PATTERN = r"(\d+),(\d+): (\d+)x(\d+)"


def parse_input(aoc_input: str):
    claims = []
    for m in re.finditer(PATTERN, aoc_input):
        x, y, w, h = m.groups()
        claims.append((int(x), int(y), int(w), int(h)))
    return claims


def count_multiclaims(claims):
    map = [[0 for _ in range(1001)] for _ in range(1001)]
    multis = 0
    for x, y, w, h in claims:
        for cx in range(x, x + w):
            for cy in range(y, y + h):
                if map[cy][cx] == 1:
                    multis += 1
                map[cy][cx] += 1
    return multis


def find_single_claims(claims):
    # build a map of the claims and keep track of the ids that have not been involved in a multiple claiming
    map = [[[] for _ in range(1001)] for _ in range(1001)]
    legit = set()

    for n, (x, y, w, h) in enumerate(claims):
        legit.add(n)

        for cx in range(x, x + w):
            for cy in range(y, y + h):
                # build map
                map[cy][cx].append(n)

                if len(map[cy][cx]) > 1:
                    # remove mmultiple claims
                    for c in map[cy][cx]:
                        if c in legit:
                            legit.remove(c)

    return legit


def solution_1(aoc_input: str):
    claims = parse_input(aoc_input)
    return count_multiclaims(claims)


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return find_single_claims(input).pop() + 1

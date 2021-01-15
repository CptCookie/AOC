MFCSAM = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

GREATER = "greater"
EXACT = "exact"
FEWER = "fewer"

RETRO = {
    "children": EXACT,
    "cats": GREATER,
    "samoyeds": EXACT,
    "pomeranians": FEWER,
    "akitas": EXACT,
    "vizslas": EXACT,
    "goldfish": FEWER,
    "trees": GREATER,
    "cars": EXACT,
    "perfumes": EXACT,
}


def parse_aunts(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n")]
    puzzle_input = [n.replace(",", "").replace(":", "").split() for n in puzzle_input]

    aunts = []
    for line in puzzle_input:
        a = {}
        for n in range(2, len(line), 2):
            a[line[n]] = int(line[n + 1])
        aunts.append(a)
    return aunts


def match(all_aunts, facts, retro=None):
    for n, aunt in enumerate(all_aunts):
        check = True

        for key in aunt:
            if retro is None:
                # check all as exact
                if aunt[key] != facts[key]:
                    check = False
            else:
                # fix retroencabulator
                if retro[key] == EXACT and aunt[key] != facts[key]:
                    check = False
                if retro[key] == GREATER and aunt[key] <= facts[key]:
                    check = False
                if retro[key] == FEWER and aunt[key] >= facts[key]:
                    check = False

        if check:
            return n + 1


def solve(puzzle_input):
    aunts = parse_aunts(puzzle_input)
    print(f"solution 1: {match(aunts, MFCSAM)}")
    print(f"solution 2: {match(aunts, MFCSAM, RETRO)}")

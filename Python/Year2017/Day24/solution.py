from collections import deque


def parse_input(aoc_input: str) -> list[(int, int)]:
    cables = []
    for line in aoc_input.splitlines():
        if line == "":
            continue
        l, r = line.split("/")
        cables.append((int(l), int(r)))
    return cables


def get_next_bridges(bridge: list[tuple], cables: list[(int, int)]):

    if len(bridge) > 1:
        connction = [c for c in bridge[-1] if c not in bridge[-2]]
        if connction:
            connction = connction[0]
        else:
            connction = bridge[-1][0]
    else:
        connction = 0

    next_bridges = []

    for cab in cables:
        if cab not in bridge and connction in cab:
            next_bridges.append([*bridge, cab])

    return next_bridges


def strength(bridge):
    return sum(sum(cable) for cable in bridge)


def get_strongest_bridge(cables: list[(int, int)]) -> int:
    q = deque()
    q.append([(0, 0)])
    max_strenth = 0

    while q:
        c_bridge = q.popleft()

        n_bridges = get_next_bridges(c_bridge, cables)

        if len(n_bridges) == 0:
            max_strenth = max(max_strenth, strength(c_bridge))

        for nb in n_bridges:
            q.append(nb)

    return max_strenth


def get_longest_bridge(cables: list[(int, int)]) -> int:
    q = deque()
    q.append([(0, 0)])
    max_strenth = 0
    max_length = 0

    while q:
        c_bridge = q.popleft()

        n_bridges = get_next_bridges(c_bridge, cables)

        if len(n_bridges) == 0:
            if (
                len(c_bridge) > max_length
                or len(c_bridge) == max_length
                and strength(c_bridge) > max_strenth
            ):
                max_strenth = strength(c_bridge)
                max_length = len(c_bridge)

        for nb in n_bridges:
            q.append(nb)

    return max_strenth


def solution_1(aoc_input: str):
    cables = parse_input(aoc_input)
    return get_strongest_bridge(cables)


def solution_2(aoc_input: str):
    cables = parse_input(aoc_input)
    return get_longest_bridge(cables)

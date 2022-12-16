from itertools import combinations
from queue import PriorityQueue


def parse_input(puzzle_input: str) -> list[str]:
    return [n for n in puzzle_input.splitlines() if n != ""]


def get_good_valves(cave_net):
    # filter valve names that actually do something
    return [name for name, cave in cave_net.items() if cave[0] > 0]

def get_valve_combs( cave_net ):
    good_valves = get_good_valves( cave_net )
    return list(combinations(good_valves, len(good_valves)))


def transform_net(cave_net):
    new_net = {}
    good_valves = get_good_valves(cave_net)
    for start in good_valves:
        new_net[start] = {}
        for end in good_valves:
            if start != end:
                new_net[start][end] = get_shortest_route(start, end, cave_net)

    return new_net

def get_shortest_route(start, end, cave_net):
    q = PriorityQueue()
    q.put((0, start))

    while q:
        l, pos = q.get()

        if end in cave_net[pos][1]:
            return l + 1

        for npos in cave_net[pos][1]:
            q.put((l+1, npos))


def calc_release(goodv_route, trans_net, cave_net):
    pass



def solution_1(puzzle_input: str):
    input = parse_input(puzzle_input)
    return None


def solution_2(puzzle_input: str):
    input = parse_input(puzzle_input)
    return None

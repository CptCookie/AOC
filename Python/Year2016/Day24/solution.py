from itertools import combinations
from queue import PriorityQueue

WALL = "#"
FLOOR = "."


def parse_map(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def find_nodes(map):
    nodes = {}
    for y, line in enumerate(map):
        for x, c in enumerate(line):
            if c.isnumeric():
                nodes[c] = (x, y)
    return nodes


def node_net_dist(map, nodes):
    net = {}

    for start, end in combinations(nodes.keys(), 2):
        dist = get_route(map, nodes[start], nodes[end])
        net[f"{start}{end}"] = dist
        net[f"{end}{start}"] = dist

    return net


def get_route(map, start, end):
    q = PriorityQueue()
    visited = {start}
    q.put((0, start))

    while not q.empty():
        dist, (cx, cy) = q.get()

        if (cx, cy) == end:
            return dist

        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy

            if (nx, ny) not in visited and map[ny][nx] != WALL:
                visited.add((nx, ny))
                q.put((dist + 1, (nx, ny)))


def get_shortest_node_path(map):
    nodes = find_nodes(map)
    node_net = node_net_dist(map, nodes)
    shortest = 10e8

    q = PriorityQueue()
    q.put((0, "0"))

    while not q.empty():
        l, path = q.get()
        if len(path) == len(nodes) and l < shortest:
            shortest = l

        for n in nodes:
            if n not in path:
                dl = node_net[f"{path[-1]}{n}"]
                q.put((l + dl, path + n))

    return shortest


def get_shortest_node_circle(map):
    nodes = find_nodes(map)
    node_net = node_net_dist(map, nodes)
    shortest = 10e8

    q = PriorityQueue()
    q.put((0, "0"))

    while not q.empty():
        l, path = q.get()
        if len(path) == len(nodes) and l + node_net[f"{path[-1]}0"] < shortest:
            shortest = l + node_net[f"{path[-1]}0"]

        for n in nodes:
            if n not in path:
                dl = node_net[f"{path[-1]}{n}"]
                q.put((l + dl, path + n))

    return shortest


def solution_1(aoc_input: str):
    input = parse_map(aoc_input)
    return get_shortest_node_path(input)


def solution_2(aoc_input: str):
    input = parse_map(aoc_input)
    return get_shortest_node_circle(input)

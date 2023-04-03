"""
plane (x,y) coordinates with x,y >= 0
start (1,1)
each coord is wall or open space
movement: vertical and horizontal
wall => number of positive bits of (x*x + 3*x + 2*x*y + y + y*y + input) % 2 == 1
open => number of positive bits of (x*x + 3*x + 2*x*y + y + y*y + input) % 2 == 0


question 1: lowest number of steps to (31,39)
"""
import heapq


def parse_data(puzzle_input: str) -> int:
    return int(puzzle_input.strip())


def is_wall(point, fav_number: int):
    x, y = point
    value = x * x + 3 * x + 2 * x * y + y + y * y + fav_number
    return bin(value).count("1") % 2 == 1


def get_man_dist(point_a: tuple[int, int], point_b: tuple[int, int]):
    return sum([sum(z) for z in zip(point_a, point_b)])


def get_adjacent_open(point: tuple[int, int], fav_number: int) -> list[tuple[int, int]]:
    adj_points = []
    for delta in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        adj = tuple(sum(z) for z in zip(point, delta))
        if all(n >= 0 for n in adj) and not is_wall(adj, fav_number):
            adj_points.append(adj)
    return adj_points


def route_len(start: tuple[int, int], end: tuple[int, int], fav_number: int):
    q = [(get_man_dist(start, end), start, 0)]
    done = set()

    while q:
        dist, point, steps = heapq.heappop(q)

        if point == end:
            return steps

        done.add(point)

        for adj in get_adjacent_open(point, fav_number):
            if adj not in done:
                heapq.heappush(q, (get_man_dist(adj, end) + steps, adj, steps + 1))


def location_at_dist(start: tuple[int, int], dist: int, fav_number: int):
    q = [(0, start)]
    done = set()

    while q:
        steps, point = heapq.heappop(q)
        done.add(point)

        if steps >= dist:
            continue

        for adj in get_adjacent_open(point, fav_number):
            if adj not in done:
                heapq.heappush(q, (steps + 1, adj))

    return len(done)


def solution_1(puzzle_input: str):
    fav_number = parse_data(puzzle_input)
    return route_len((1, 1), (31, 39), fav_number)


def solution_2(puzzle_input: str):
    fav_number = parse_data(puzzle_input)
    return location_at_dist((1, 1), 50, fav_number)

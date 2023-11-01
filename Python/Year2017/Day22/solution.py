from copy import deepcopy

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

INFECTED = "#"
WEAK = "W"
FLAG = "F"


def parse_input(aoc_input: str) -> (list[(int, int)], (int, int)):
    # just collect the infected nodes and the center position
    grid = [n for n in aoc_input.splitlines() if n != ""]
    center = (len(grid[0]) // 2, len(grid) // 2)
    infections = set(
        (x, y)
        for y, line in enumerate(grid)
        for x, c in enumerate(line)
        if c == INFECTED
    )

    return infections, center


def iterate_grid(infected: set, virus_start, iterations):
    virus_pos = virus_start
    virus_dir = 0
    n_infects = 0

    for i in range(iterations):

        if virus_pos in infected:
            virus_dir = (virus_dir + 1) % 4
            infected.remove(virus_pos)

        else:
            virus_dir = (virus_dir + 4 - 1) % 4
            infected.add(virus_pos)
            n_infects += 1

        virus_pos = (
            virus_pos[0] + DIRECTIONS[virus_dir][0],
            virus_pos[1] + DIRECTIONS[virus_dir][1],
        )

    return n_infects


def evolved_iterate_grid(infected: set, virus_start, iterations):
    virus_pos = virus_start
    virus_dir = 0

    grid = {pos: "#" for pos in infected}
    n_infects = 0

    for i in range(iterations):
        match grid.get(virus_pos):
            case None:
                # clean
                virus_dir = (virus_dir + 4 - 1) % 4
                grid[virus_pos] = WEAK

            case x if x == WEAK:
                grid[virus_pos] = INFECTED
                n_infects += 1

            case x if x == INFECTED:
                virus_dir = (virus_dir + 1) % 4
                grid[virus_pos] = FLAG

            case x if x == FLAG:
                virus_dir = (virus_dir + 2) % 4
                del grid[virus_pos]

        virus_pos = (
            virus_pos[0] + DIRECTIONS[virus_dir][0],
            virus_pos[1] + DIRECTIONS[virus_dir][1],
        )

    return n_infects


def solution_1(aoc_input: str):
    infections, center = parse_input(aoc_input)
    n_infects = iterate_grid(infections, center, 10000)
    return n_infects


def solution_2(aoc_input: str):
    infections, center = parse_input(aoc_input)
    n_infects = evolved_iterate_grid(infections, center, 10000000)
    return n_infects

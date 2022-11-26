def get_path(cable_input):
    path = [(0, 0)]
    for step in cable_input:

        if step[0] == "R":
            path += [
                (path[-1][0] + n, path[-1][1]) for n in range(1, int(step[1:]) + 1)
            ]
        elif step[0] == "L":
            path += [
                (path[-1][0] - n, path[-1][1]) for n in range(1, int(step[1:]) + 1)
            ]
        elif step[0] == "U":
            path += [
                (path[-1][0], path[-1][1] + n) for n in range(1, int(step[1:]) + 1)
            ]
        elif step[0] == "D":
            path += [
                (path[-1][0], path[-1][1] - n) for n in range(1, int(step[1:]) + 1)
            ]

    return path[1:]


def get_closest_intersection_distance(cable_path_1, cable_path_2):
    intersections = set(cable_path_1) & set(cable_path_2)
    return min([abs(n[0]) + abs(n[1]) for n in intersections])


def get_shortest_intersection_steps_comb(cable_path_1, cable_path_2):
    intersections = set(cable_path_1) & set(cable_path_2)
    intersections_steps = [
        cable_path_1.index(n) + cable_path_2.index(n) + 2 for n in intersections
    ]

    return min(intersections_steps)


def solution_1(puzzle_input):
    cables = puzzle_input.split("\n")
    cable_1 = get_path(cables[0].split(","))
    cable_2 = get_path(cables[1].split(","))
    return get_closest_intersection_distance(cable_1, cable_2)


def solution_2(puzzle_input):
    cables = puzzle_input.split("\n")
    cable_1 = get_path(cables[0].split(","))
    cable_2 = get_path(cables[1].split(","))

    return get_shortest_intersection_steps_comb(cable_1, cable_2)

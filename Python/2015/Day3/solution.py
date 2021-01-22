UP = "^"
DOWN = "v"
LEFT = "<"
RIGHT = ">"


def map_moves(puzzel_input):
    pos = [[0, 0]]
    for direction in puzzel_input:
        current = pos[-1]
        if direction is UP:
            pos.append([current[0], current[1] + 1])
        elif direction is DOWN:
            pos.append([current[0], current[1] - 1])
        elif direction is RIGHT:
            pos.append([current[0] + 1, current[1]])
        elif direction is LEFT:
            pos.append([current[0] - 1, current[1]])
    return pos


def get_unique(lst: []):
    return [x for n, x in enumerate(lst) if lst.index(x) == n]


def solution_1(puzzle_input):
    return len(get_unique(map_moves(puzzle_input)))


def solution_2(puzzle_input):
    santa = puzzle_input[::2]
    robo = puzzle_input[1::2]
    return len(get_unique(map_moves(santa) + map_moves(robo)))

def sum_up(puzzle_input):
    return sum([1 if n == "(" else -1 for n in puzzle_input])


def enter_basement(puzzle_input):
    floor = 0
    puzzle_input = [1 if n == "(" else -1 for n in puzzle_input]
    for n, c in enumerate(puzzle_input):
        floor += int(c)
        if floor < 0:
            return n + 1


def solution_1(puzzle_input):
    return sum_up(puzzle_input)


def solution_2(puzzle_input):
    return enter_basement(puzzle_input)

def two_numbers(puzzle_input):
    for n in puzzle_input:
        for m in puzzle_input:
            if n + m == 2020:
                return n * m


def three_numbers(puzzle_input):
    for n in puzzle_input:
        for m in puzzle_input:
            for o in puzzle_input:
                if n + m + o == 2020:
                    return n * m * o


def solution_1(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.split("\n") if n != ""]
    return two_numbers(puzzle_input)


def solution_2(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.split("\n") if n != ""]
    return three_numbers(puzzle_input)

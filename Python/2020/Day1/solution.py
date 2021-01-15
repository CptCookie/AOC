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


def solve(puzzle_input):
    puzzle_input = [int(n) for n in puzzle_input.split("\n") if n != ""]
    print(f"solution 1: {two_numbers(puzzle_input)}")
    print(f"solution 2: {three_numbers(puzzle_input)}")

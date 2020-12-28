def sum_up(puzzle_input):
    return sum([1 if n=='(' else -1 for n in puzzle_input])

def enter_basement(puzzle_input):
    floor = 0
    puzzle_input = [1 if n=='(' else -1 for n in puzzle_input]
    for n, c in enumerate(puzzle_input):
        floor += int(c)
        if floor < 0:
            return n+1

def solve(puzzle_input):
    print(sum_up(puzzle_input))
    print(enter_basement(puzzle_input))
    
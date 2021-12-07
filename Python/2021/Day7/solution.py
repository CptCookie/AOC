import statistics


def solution_1(puzzle_input: str):
    puzzle_data = [int(n) for n in puzzle_input.replace("\n", "").split(",")]
    alignment = statistics.median(puzzle_data)
    return sum([abs(i - alignment) for i in puzzle_data])


def solution_2(puzzle_input: str):
    puzzle_data = [int(n) for n in puzzle_input.replace("\n", "").split(",")]
    alignment = int(statistics.mean(puzzle_data))
    return min(
        sum(abs(i - a) * (abs(i - a) + 1) / 2 for i in puzzle_data)
        for a in [alignment, alignment + 1]
    )

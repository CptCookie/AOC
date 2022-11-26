def simulate_day(lanternfisch: list[int]) -> list[int]:
    new_lanternfish = [0] * 9
    for index in range(len(lanternfisch)):
        if index == 0:
            new_lanternfish[6] += lanternfisch[0]
            new_lanternfish[8] += lanternfisch[0]
        else:
            new_lanternfish[index - 1] += lanternfisch[index]
    return new_lanternfish


def parse_lanternfish(puzzle_input):
    lanternfish = [0] * 9
    for i in puzzle_input.split(","):
        lanternfish[int(i)] += 1
    return lanternfish


def solution_1(puzzle_input: str):
    lanternfish = parse_lanternfish(puzzle_input)
    for i in range(80):
        lanternfish = simulate_day(lanternfish)
    return sum(lanternfish)


def solution_2(puzzle_input: str):
    lanternfish = parse_lanternfish(puzzle_input)
    for i in range(256):
        lanternfish = simulate_day(lanternfish)
    return sum(lanternfish)

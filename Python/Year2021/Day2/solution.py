def parse_input(puzzle_input: str):
    puzzle_data = [n.split(" ") for n in puzzle_input.splitlines() if n != ""]
    return puzzle_data


def solution_1(puzzle_input: str):
    puzzle_data = parse_input(puzzle_input)
    horizontal = sum([int(n[1]) for n in puzzle_data if n[0] == "forward"])
    verticaly_up = sum([int(n[1]) for n in puzzle_data if n[0] == "up"])
    verticaly_down = sum([int(n[1]) for n in puzzle_data if n[0] == "down"])
    print(horizontal, verticaly_up, verticaly_down)
    return horizontal * (verticaly_up - verticaly_down)


def solution_2(puzzle_input: str):
    puzzle_data = parse_input(puzzle_input)
    aim, x, y = 0, 0, 0
    for cmd, dist in puzzle_data:
        if cmd == "up":
            aim += int(dist)
        elif cmd == "down":
            aim -= int(dist)
        elif cmd == "forward":
            x += int(dist)
            y += int(dist) * aim
    return x * y

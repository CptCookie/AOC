def parse_range(string: str):
    r = string.split(" ")[0].split("-")
    return range(int(r[0]), int(r[1]) + 1)


def parse_positions(string: str):
    r = string.split(" ")[0].split("-")
    return (int(r[0]) - 1, int(r[1]) - 1)


def parse_letter(string: str):
    return string.split(" ")[1]


def count_old_policy(data_input):
    counter = 0
    for param, string in data_input:
        if string.count(parse_letter(param)) in parse_range(param):
            counter += 1
    return counter


def count_new_policy(data_input):
    counter = 0
    for param, string in data_input:
        pos_1, pos_2 = parse_positions(param)
        letter = parse_letter(param)
        if (string[pos_1] == letter) ^ (string[pos_2] == letter):
            counter += 1
    return counter


def solve(puzzle_input):
    puzzle_input = [n.split(": ") for n in puzzle_input.split("\n") if n != ""]
    print(f"solution 1: {count_old_policy(puzzle_input)}")
    print(f"solution 2: {count_new_policy(puzzle_input)}")

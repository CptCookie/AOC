def is_not_descending(password: int):
    pass_str = str(password)
    for n, digit in enumerate(pass_str[1:]):
        if int(digit) < int(pass_str[n]):
            return False
    return True


def contains_multiple(password: int):
    for n in range(10):
        if str(n) + str(n) in str(password):
            return True
    return False


def contains_double(password: int):
    pass_str = str(password)
    for n in range(10):
        if f"{n}{n}" in pass_str and not f"{n}{n}{n}" in pass_str:
            return True
    return False


def is_valid_v1(password: int):
    return contains_multiple(password) and is_not_descending(password)


def is_valid_v2(password: int):
    return contains_double(password) and is_not_descending(password)


def solution_1(puzzle_input):
    boundries = [int(n) for n in puzzle_input.split("-")]
    valid = [n for n in range(boundries[0], boundries[1] + 1) if is_valid_v1(n)]
    return len(valid)


def solution_2(puzzle_input):
    boundries = [int(n) for n in puzzle_input.split("-")]
    valid = [n for n in range(boundries[0], boundries[1] + 1) if is_valid_v2(n)]
    return len(valid)

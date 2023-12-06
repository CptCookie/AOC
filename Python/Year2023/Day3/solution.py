import math

NEIGHBORS = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def parse_input(aoc_input: str):
    symbols = []
    numbers = []
    for y, line in enumerate(aoc_input.splitlines()):
        num_start = None
        for x, c in enumerate(line):
            if not c.isdigit() and c != ".":
                symbols.append((c, (x, y)))

            if c.isdigit() and num_start is None:
                num_start = x

            if num_start is not None and not c.isdigit():
                num = int(line[num_start:x])
                numbers.append((num, (num_start, y)))
                num_start = None

        if num_start:
            num = int(line[num_start:])
            numbers.append((num, (num_start, y)))

    return numbers, symbols


def number_close_pos(num_start, num, pos) -> bool:
    num_len = int(math.log10(num)) + 1
    for dx in range(num_len):
        for nx, ny in NEIGHBORS:
            if num_start[0] + dx + nx == pos[0] and num_start[1] + ny == pos[1]:
                return True
    return False


def solution_1(aoc_input: str):
    numbers, symbols = parse_input(aoc_input)

    sum_close = 0
    for number, pos in numbers:
        if any(number_close_pos(pos, number, s[1]) for s in symbols):
            sum_close += number

    return sum_close


def solution_2(aoc_input: str):
    numbers, symbols = parse_input(aoc_input)
    sum_ratio = 0

    for sym, sym_pos in symbols:
        if sym == "*":
            close_nums = [
                num
                for num, num_pos in numbers
                if number_close_pos(num_pos, num, sym_pos)
            ]
            if len(close_nums) == 2:
                sum_ratio += close_nums[0] * close_nums[1]
    return sum_ratio

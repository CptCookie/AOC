import math

NEIGHBORS = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))


def parse_input(aoc_input: str):
    symbols = set()
    numbers = {}
    for y, line in enumerate(aoc_input.splitlines()):
        for x, c in enumerate(line):
            if not c.isdigit() and c != ".":
                symbols.add((x, y))

            if x == 0 and c.isdigit() or c.isdigit() and line[x - 1] == ".":
                n = "".join(
                    [
                        line[nx]
                        for nx in range(x, min(x + 3, len(line) - 1))
                        if line[nx].isdigit()
                    ]
                )
                numbers[int(n)] = (x, y)

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
    sum = 0

    for n in numbers:
        if any(number_close_pos(numbers[n], n, s) for s in symbols):
            print(n)
            sum += n

    return sum


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return None

def solution_1(puzzle_input: str) -> int:
    skip = int(puzzle_input.strip())
    pos = 0
    buffer = [0]

    for i in range(1, 2017 + 1):
        pos = (pos + skip) % len(buffer)
        buffer.insert(pos + 1, i)
        pos = pos + 1

    return buffer[pos + 1]


def solution_2(puzzle_input: str):
    skip = int(puzzle_input.strip())
    pos = 0
    latest = 0

    for i in range(1, 50_000_000 + 1):
        pos = (pos + skip) % i + 1
        if pos == 1:
            latest = i

    return latest

DIRECTIONS = (
    (-1, 0),  # W
    (1, 0),  # E
    (0, -1),  # N
    (0, 1),  # S
    (-1, -1),  # NW
    (1, -1),  # NE
    (-1, 1),  # SW
    (1, 1),  # SE
)

MAS_POS = (
    # Word 1
    ((-1, -1), (0, 0), (1, 1)),
    # Word 2
    ((1, -1), (0, 0), (-1, 1)),
)


def parse_input(aoc_input: str) -> list[str]:
    return [n for n in aoc_input.splitlines() if n != ""]


def iterate_direction(x: int, y: int, dx: int, dy: int):
    for n in range(4):
        yield x + dx * n, y + dy * n


def get_directional_words(x: int, y: int, puzzle: list[str]):
    words = []
    for dx, dy in DIRECTIONS:
        if not 0 <= x + dx * 3 < len(puzzle[0]) or not 0 <= y + dy * 3 < len(puzzle):
            continue

        letters = []
        for nx, ny in iterate_direction(x, y, dx, dy):
            letters.append(puzzle[ny][nx])
        words.append("".join(letters))
    return words


def is_x_mas(x: int, y: int, puzzle: list[str]):
    for word_dir in MAS_POS:
        word = []
        for dx, dy in word_dir:
            nx, ny = x + dx, y + dy
            try:
                word.append(puzzle[ny][nx])
            except IndexError:
                return False

        if not word == ["M", "A", "S"] and not word == ["S", "A", "M"]:
            return False

    return True


def solution_1(aoc_input: str):
    input = parse_input(aoc_input)
    count = 0

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "X":
                words: list[str] = get_directional_words(x, y, input)
                count += words.count("XMAS")
                count += words.count("SAMX")
    return count


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    count = 0

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "A" and is_x_mas(x, y, input):
                count += 1
    return count

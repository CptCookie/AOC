import re


def parse_points(puzzle_input: str) -> list[tuple[int]]:
    all_points = []
    for point in re.findall(r"(\d+),(\d+)", puzzle_input):
        all_points.append((int(point[0]), int(point[1])))
    return all_points


def parse_instuctions(puzzle_input: str) -> list[tuple[str]]:
    return re.findall(r"fold along ([xy])=(\d+)", puzzle_input)


def build_paper(points: list[tuple[int]]) -> list[list[bool]]:
    w_max = max(n[0] for n in points)
    h_max = max(n[1] for n in points)
    paper = [[False] * (w_max + 1) for _ in range(h_max + 1)]

    for x, y in points:
        paper[y][x] = True
    return paper


def fold_x(paper: list[list[bool]], fold_x: int) -> list[list[bool]]:
    new_paper = [[False] * fold_x for _ in range(len(paper))]

    for y, line in enumerate(new_paper):
        for x in range(len(line)):
            if fold_x - x <= len(paper[0]) - fold_x - 1:
                new_paper[y][x] = paper[y][x] or paper[y][2 * fold_x - x]
            else:
                new_paper[y][x] = paper[y][x]
    return new_paper


def fold_y(paper: list[list[bool]], fold_y: int) -> list[list[bool]]:
    new_paper = [[False] * (len(paper[0])) for _ in range(fold_y)]

    for y in range(len(new_paper)):
        if fold_y - y <= len(paper) - fold_y - 1:
            new_paper[y] = [
                og or fold for og, fold in zip(paper[y], paper[2 * fold_y - y])
            ]
        else:
            new_paper[y] = paper[y]
    return new_paper


def print_paper(paper: list[list[bool]]):
    for line in paper:
        for c in line:
            if c:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def solution_1(puzzle_input: str):
    paper = build_paper(parse_points(puzzle_input))
    folds = parse_instuctions(puzzle_input)

    if folds[0][0] == "x":
        paper = fold_x(paper, int(folds[0][1]))
    else:
        paper = fold_y(paper, int(folds[0][1]))

    return sum(sum(line) for line in paper)


def solution_2(puzzle_input: str):
    paper = build_paper(parse_points(puzzle_input))
    folds = parse_instuctions(puzzle_input)

    for f in folds:
        if f[0] == "x":
            paper = fold_x(paper, int(f[1]))
        else:
            paper = fold_y(paper, int(f[1]))
    print_paper(paper)
    return sum(sum(line) for line in paper)

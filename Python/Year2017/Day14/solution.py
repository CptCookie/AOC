from year_2017.Day10.solution import solution_2 as knot_hash

Disk = list[list[str | int]]


def build_disk_image(image_hash: str) -> Disk:
    disc = []
    for l in range(128):
        line = []
        hashed = knot_hash(f"{image_hash}-{l}")
        for c in "{0:0>128}".format(bin(int(hashed, 16))[2:]):
            line.append("#" if c == "1" else ".")
        disc.append(line)
    return disc


def search_clusters(disc: Disk) -> tuple[Disk, int]:
    clusters_found = 0
    for y, line in enumerate(disc):
        for x, block in enumerate(line):
            if block == "#":
                clusters_found += 1
                disc = mark_cluster(disc, (x, y), clusters_found)

    return disc, clusters_found


def mark_cluster(disc: Disk, point: tuple[int, int], number: int) -> Disk:
    marking_open = {point}
    marked = {}

    while marking_open:
        x, y = marking_open.pop()
        print(x, y)
        disc[y][x] = number

        for p in get_adjacent((x, y)):
            is_px_in = 0 <= p[0] < len(disc[0])
            is_py_in = 0 <= p[1] < len(disc)
            is_valid = is_px_in and is_py_in and disc[p[1]][p[0]] == "#"
            if p not in marked and is_valid:
                marking_open.add(p)
    return disc


def get_adjacent(point: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = point
    return [(x + dx, y + dy) for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]]


def solution_1(puzzle_input: str):
    total_on = 0
    disc = build_disk_image(puzzle_input.strip())
    for line in disc:
        total_on += line.count("#")
    return total_on


def solution_2(puzzle_input: str):
    disc = build_disk_image(puzzle_input.strip())
    _, found = search_clusters(disc)
    return found

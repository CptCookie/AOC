Pos = tuple[int, int]


DIRECTIONS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def parse_input(aoc_input: str) -> (list[Pos], list[Pos], Pos, list[str]):
    walls = set()
    boxes = set()
    instr = []
    robot = None

    for y, line in enumerate(aoc_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case "#":
                    walls.add((x, y))
                case "O":
                    boxes.add((x, y))
                case "@":
                    robot = (x, y)
                case d if d in DIRECTIONS:
                    instr.append(d)

    return walls, boxes, robot, instr


def parse_input_wide(aoc_input: str) -> (list[Pos], list[Pos], Pos, list[str]):
    walls = set()
    boxes = set()
    instr = []
    robot = None

    for y, line in enumerate(aoc_input.splitlines()):
        for x, c in enumerate(line):
            match c:
                case "#":
                    walls.add((2 * x, y))
                    walls.add((2 * x + 1, y))
                case "O":
                    boxes.add((2 * x, y))
                case "@":
                    robot = (x, y)
                case d if d in DIRECTIONS:
                    instr.append(d)

    return walls, boxes, robot, instr


def push(pos, direction, walls: set[Pos], boxes: set[Pos]):
    x, y = pos
    dx, dy = DIRECTIONS[direction]
    nx, ny = x + dx, y + dy

    if pos in walls:
        raise ValueError("can not push into walls")

    if pos not in boxes:
        return

    push((nx, ny), direction, walls, boxes)
    boxes.remove((x, y))
    boxes.add((nx, ny))


def get_wide_box(pos: Pos, boxes: set[Pos]):
    if pos in boxes:
        return pos
    if (pos[0] - 1, pos[1]) in boxes:
        return pos[0] - 1, pos[1]


def gps_value(box: Pos) -> int:
    return box[0] + box[1] * 100


def follow_instructions(robot: Pos, boxes: set[Pos], walls: set[Pos], instr: list[str]):
    for dir in instr:
        rx, ry = robot
        dx, dy = DIRECTIONS[dir]

        try:
            push((rx + dx, ry + dy), dir, walls, boxes)
            robot = (rx + dx, ry + dy)
        except ValueError:
            pass


def solution_1(aoc_input: str):
    walls, boxes, robot, instr = parse_input(aoc_input)
    follow_instructions(robot, boxes, walls, instr)
    return sum(gps_value(b) for b in boxes)


def solution_2(aoc_input: str):
    input = parse_input(aoc_input)
    return None

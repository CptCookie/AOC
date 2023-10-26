CORNER = "+"
VERTICAL = "|"
HORIZONTAL = "-"
SPACE = " "


def parse_routing(aoc_input) -> list[str]:
    return [line for line in aoc_input.splitlines() if line != ""]


def get_start_pos(routing):
    for x, c in enumerate(routing[0]):
        if c == VERTICAL:
            return (x, 0)


def get_routing_code(routing):
    start = get_start_pos(routing)
    code = ""
    steps = 0
    orient = VERTICAL

    pos = start
    max_y = len(routing) - 1
    max_x = len(routing[0]) - 1

    while True:
        x, y = pos

        if orient == VERTICAL and (y == 0 or routing[y - 1][x] == SPACE):
            dx, dy = (0, 1)
        elif orient == VERTICAL and (y == max_y or routing[y + 1][x] == SPACE):
            dx, dy = (0, -1)
        elif orient == HORIZONTAL and (x == 0 or routing[y][x - 1] == SPACE):
            dx, dy = (1, 0)
        elif orient == HORIZONTAL and (x == max_x or routing[y][x + 1] == SPACE):
            dx, dy = (-1, 0)
        else:
            raise ValueError("WHERE THE F ARE WE?")

        cx, cy = x + dx, y + dy
        steps += 1

        while True:
            sym = routing[cy][cx]

            if sym == CORNER:
                orient = HORIZONTAL if orient == VERTICAL else VERTICAL
                break

            elif sym == SPACE:
                # move one step back, we found the end of the route
                return code, steps

            elif sym.isalpha():
                code += sym

            cx, cy = cx + dx, cy + dy
            steps += 1

        pos = cx, cy


def solution_1(aoc_input: str):
    routing = parse_routing(aoc_input)
    return get_routing_code(routing)[0]


def solution_2(puzzle_input: str):
    routing = parse_routing(puzzle_input)
    return get_routing_code(routing)[1]

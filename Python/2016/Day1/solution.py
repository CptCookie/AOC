NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"

DIRECTIONS = [NORTH, EAST, SOUTH, WEST]


class Routing:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = NORTH
        self.visited = [(0, 0)]

    def distance_from_start(self):
        return abs(self.x) + abs(self.y)

    def turn_right(self):
        self._turn(1)

    def turn_left(self):
        self._turn(-1)

    def _turn(self, turn):
        new_dir_index = (DIRECTIONS.index(self.direction) + turn) % 4
        self.direction = DIRECTIONS[new_dir_index]

    def move(self, distance):
        if self.direction == NORTH:
            self.visited.extend(
                [(self.x, n) for n in range(self.y + 1, self.y + distance + 1)]
            )
            self.y += distance
        elif self.direction == EAST:
            self.visited.extend(
                [(n, self.y) for n in range(self.x + 1, self.x + distance + 1)]
            )
            self.x += distance
        elif self.direction == SOUTH:
            self.visited.extend(
                [(self.x, n) for n in range(self.y - 1, self.y - distance - 1, -1)]
            )
            self.y -= distance
        elif self.direction == WEST:
            self.visited.extend(
                [(n, self.y) for n in range(self.x - 1, self.x - distance - 1, -1)]
            )
            self.x -= distance

    def fist_double_visited(self):
        for n, location in enumerate(self.visited):
            if self.visited.index(location) != n:
                return location


def solution_1(puzzle_input):
    puzzle_input = puzzle_input.replace("\n", "").split(", ")
    route = Routing()

    for p in puzzle_input:
        if p[0] == "R":
            route.turn_right()
        if p[0] == "L":
            route.turn_left()
        route.move(int(p[1:]))

    return route.distance_from_start()


def solution_2(puzzle_input):
    puzzle_input = puzzle_input.replace("\n", "").split(", ")
    route = Routing()

    for p in puzzle_input:
        if p[0] == "R":
            route.turn_right()
        if p[0] == "L":
            route.turn_left()
        route.move(int(p[1:]))

    fist_double_location = route.fist_double_visited()
    return fist_double_location[0] + fist_double_location[1]

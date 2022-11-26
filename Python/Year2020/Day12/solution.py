import requests


DIRECTIONS = ["N", "E", "S", "W"]
ROTATION = ["R", "L"]
FORWARD = "F"


class Ship:
    def __init__(self, waypoint_nav=False):
        self.north = 0
        self.east = 0
        self.direction = "E"
        self.waypoint_nav = waypoint_nav
        self.waypoint_north = 1
        self.waypoint_east = 10

    @property
    def distance(self):
        return abs(self.north) + abs(self.east)

    @property
    def pos(self):
        return (self.east, self.north)

    @property
    def way_pos(self):
        return (self.waypoint_east, self.waypoint_north)

    def move_direction(self, direction, distance):
        if direction == "N":
            if self.waypoint_nav:
                self.waypoint_north += distance
            else:
                self.north += distance
        elif direction == "S":
            if self.waypoint_nav:
                self.waypoint_north -= distance
            else:
                self.north -= distance
        elif direction == "E":
            if self.waypoint_nav:
                self.waypoint_east += distance
            else:
                self.east += distance
        elif direction == "W":
            if self.waypoint_nav:
                self.waypoint_east -= distance
            else:
                self.east -= distance

    def rotate(self, clockwise, degree):
        if self.waypoint_nav:
            if degree == 180:
                self.waypoint_east, self.waypoint_north = (
                    -self.waypoint_east,
                    -self.waypoint_north,
                )
            elif clockwise and degree == 90 or not clockwise and degree == 270:
                self.waypoint_east, self.waypoint_north = (
                    self.waypoint_north,
                    -self.waypoint_east,
                )
            elif not clockwise and degree == 90 or clockwise and degree == 270:
                self.waypoint_east, self.waypoint_north = (
                    -self.waypoint_north,
                    self.waypoint_east,
                )
        else:
            if clockwise:
                self.direction = DIRECTIONS[
                    (DIRECTIONS.index(self.direction) + int(degree / 90)) % 4
                ]
            else:
                self.direction = DIRECTIONS[
                    (DIRECTIONS.index(self.direction) - int(degree / 90)) % 4
                ]

    def forward(self, distance):
        if self.waypoint_nav:
            self.north += self.waypoint_north * distance
            self.east += self.waypoint_east * distance
        else:
            self.move_direction(self.direction, distance)

    def manouver(self, manovers: [str]):
        for move in manovers:
            if move[0] in DIRECTIONS:
                self.move_direction(move[0], int(move[1:]))
            elif move[0] in ROTATION:
                self.rotate(move[0] == "R", int(move[1:]))
            elif move[0] == FORWARD:
                self.forward(int(move[1:]))


def solve(puzzle_input):
    puzzle_input = [n for n in puzzle_input.split("\n") if n != ""]
    ship = Ship()
    ship.manouver(puzzle_input)
    print(f"solution 1: {ship.distance}")

    ship = Ship(waypoint_nav=True)
    ship.manouver(puzzle_input)
    print(f"solution 2: {ship.distance}")
